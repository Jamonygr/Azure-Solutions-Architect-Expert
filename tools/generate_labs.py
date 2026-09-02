#!/usr/bin/env python3
"""Generate complete portable labs from the frozen AZ-305 curriculum contracts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Optional

from az305lib import ROOT, domain_name, load_model, markdown_escape, objective_map, ps_single, write_or_check, yaml_text

VALID_COSTS = {"none", "low", "moderate", "elevated"}


def checkpoint_objectives(objectives: list[str], checkpoint_index: int) -> list[str]:
    if len(objectives) <= 5:
        return [objectives[(checkpoint_index - 1) % len(objectives)]]
    return [objective for position, objective in enumerate(objectives) if position % 5 == checkpoint_index - 1]


def requirement_document(lab: dict[str, Any], content: dict[str, Any], objectives: list[str]) -> dict[str, Any]:
    functional = []
    nonfunctional = []
    for index, checkpoint in enumerate(content["checkpoints"], 1):
        entry = {
            "id": checkpoint["requirement"],
            "statement": checkpoint["expected"],
            "mandatory": True,
            "objectiveIds": checkpoint_objectives(objectives, index),
        }
        (functional if index <= 3 else nonfunctional).append(entry)
    number = lab["number"]
    analysis = content["architectureAnalysis"]
    change_requirement = analysis["revisedDecision"]["mandatoryRequirementId"]
    requirement_ids = {checkpoint["requirement"] for checkpoint in content["checkpoints"]}
    if change_requirement not in requirement_ids:
        raise ValueError(f"{lab['id']} revised decision cites unknown requirement {change_requirement}")
    return {
        "schemaVersion": "1.0.0",
        "labId": lab["id"],
        "businessOutcome": content["businessOutcome"],
        "stakeholders": content["stakeholders"],
        "functionalRequirements": functional,
        "nonfunctionalRequirements": nonfunctional,
        "constraints": [*analysis["constraints"],
            f"Use only the {lab['laneLabel']} command lane for learner implementation.",
            "Keep all live changes behind explicit execution and acknowledgement switches.",
            "Retain only sanitized command evidence and synthetic fixture identifiers.",
        ],
        "assumptions": [*analysis["assumptions"],
            "West Europe is the configurable primary example and North Europe is the configurable secondary example.",
            "The learner has administrator-level Azure operations knowledge but receives no pre-existing authenticated context.",
            "Offline fixtures demonstrate contract behavior rather than live Azure service behavior.",
        ],
        "facts": analysis["facts"],
        "acceptanceCriteria": [
            f"{checkpoint['requirement']} passes its independent positive and negative assertions."
            for checkpoint in content["checkpoints"]
        ],
        "changeRequest": {
            "id": f"LAB{number}-CR-01",
            "trigger": content["changeRequest"],
            "materialChange": content["changeRequest"],
            "mandatoryRequirementId": change_requirement,
            "expectedRevision": analysis["changeExpectedRevision"],
        },
    }


def decision_document(lab: dict[str, Any], content: dict[str, Any], objectives: list[str]) -> dict[str, Any]:
    criteria = [
        {"id": "C1", "name": "Mandatory requirements fit", "weight": 30},
        {"id": "C2", "name": "Reliability and recovery", "weight": 25},
        {"id": "C3", "name": "Security and governance", "weight": 20},
        {"id": "C4", "name": "Operational manageability", "weight": 15},
        {"id": "C5", "name": "Cost and performance efficiency", "weight": 10},
    ]
    analysis = content["architectureAnalysis"]
    selected_name = content["selected"]
    candidates = []
    for index, authored in enumerate(analysis["candidateAnalyses"]):
        scores = dict(authored["scores"])
        total = sum(criterion["weight"] * scores[criterion["id"]] for criterion in criteria) / 5
        candidates.append({
            "id": f"CAND-{chr(65 + index)}",
            "name": authored["name"],
            "eligible": authored["eligible"],
            "disqualifiers": list(authored["disqualifiers"]),
            "scores": scores,
            "weightedTotal": total,
            "rationale": authored["rationale"],
        })
    names = {candidate["name"] for candidate in candidates}
    if not set(content["candidates"]).issubset(names):
        raise ValueError(f"{lab['id']} architecture analysis omits an authored candidate")
    if selected_name not in names:
        raise ValueError(f"{lab['id']} selected candidate is not in the architecture analysis")
    revised = analysis["revisedDecision"]
    if revised["selectedCandidate"] not in names:
        raise ValueError(f"{lab['id']} revised candidate is not in the architecture analysis")
    authored_by_name = {item["name"]: item for item in analysis["candidateAnalyses"]}
    number = lab["number"]
    return {
        "schemaVersion": "1.0.0",
        "labId": lab["id"],
        "implementationMode": lab["implementationMode"],
        "criteria": criteria,
        "candidates": candidates,
        "selectedCandidate": selected_name,
        "rejectedAlternatives": [
            {"candidate": item["name"], "reason": authored_by_name[item["name"]]["rejectedReason"]}
            for item in candidates if item["name"] != selected_name
        ],
        "risks": analysis["risks"],
        "waf": analysis["waf"],
        "safeAnalogue": analysis["safeAnalogue"],
        "traceability": [
            {"objectiveId": objective, "requirementId": cp["requirement"], "checkpointId": f"LAB{number}-CP0{index}"}
            for index, cp in enumerate(content["checkpoints"], 1)
            for objective in checkpoint_objectives(objectives, index)
        ],
        "adr": {
            "id": f"ADR-LAB{number}-001",
            "status": "accepted",
            "context": content["scenario"],
            "decision": f"Select {selected_name}: {authored_by_name[selected_name]['rationale']}",
            "consequences": analysis["adrConsequences"],
        },
        "revisedDecision": {
            "changeRequestId": f"LAB{number}-CR-01",
            "selectedCandidate": revised["selectedCandidate"],
            "reason": revised["reason"],
            "mandatoryRequirementId": revised["mandatoryRequirementId"],
            "waf": revised["waf"],
        },
    }


def discover_inputs(content: dict[str, Any]) -> list[str]:
    source = "\n".join(
        str(checkpoint.get(field, ""))
        for checkpoint in content["checkpoints"]
        for field in ("command", "positiveCommand", "negativeCommand")
    )
    names = set(re.findall(r"(?<!\$)\$([A-Za-z_][A-Za-z0-9_]*)", source))
    assigned = set(re.findall(r"\$([A-Za-z_][A-Za-z0-9_]*)\s*=", source))
    assigned.update(re.findall(r"(?i)foreach\s*\(\s*\$([A-Za-z_][A-Za-z0-9_]*)\s+in\b", source))
    names.difference_update(assigned)
    excluded = {
        "SubscriptionId", "TenantId", "RunId", "Location", "SecondaryLocation", "ResourceGroup", "WorkloadName",
        "Execute", "AcknowledgeCost", "AcknowledgeTenantChange", "ExpiresOn", "true", "false", "null", "env",
        "PSVersionTable", "PSScriptRoot", "ErrorActionPreference", "LASTEXITCODE", "_", "input", "args", "matches",
    }
    return sorted(name for name in names if name not in excluded)


def lab_metadata(lab: dict[str, Any], content: dict[str, Any], objectives: list[str]) -> dict[str, Any]:
    number = lab["number"]
    return {
        "schemaVersion": "1.0.0", "id": lab["id"], "number": int(number), "slug": lab["folder"],
        "title": lab["title"], "domain": domain_name(lab["domainId"]), "track": lab["track"],
        "implementationMode": lab["implementationMode"], "status": "offline-validated", "role": content["role"],
        "outcome": content["outcome"], "duration": content["duration"], "difficulty": content["difficulty"],
        "costClass": content["costClass"] if content["costClass"] in VALID_COSTS else "moderate",
        "permissions": content["architectureAnalysis"]["permissions"],
        "licensing": content["architectureAnalysis"]["licensing"],
        "safeAnalogue": lab["implementationMode"] != "reference-deployable",
        "sourceUrls": [content["primarySource"]["url"]],
        "objectives": {"primary": list(lab["primaryObjectiveIds"]), "reinforced": objectives if lab.get("reinforcesAllOfficialObjectives") else []},
        "inputs": ["SubscriptionId", "TenantId", "RunId", "Location", "SecondaryLocation", "ResourceGroup", "WorkloadName", "ExpiresOn", *discover_inputs(content), "Execute", "AcknowledgeCost", "AcknowledgeTenantChange"],
        "checkpoints": [
            {"id": f"LAB{number}-CP0{index}", "title": cp["title"], "requirementIds": [cp["requirement"]], "objectiveIds": checkpoint_objectives(objectives, index)}
            for index, cp in enumerate(content["checkpoints"], 1)
        ],
        "assessment": {"enabled": 1 <= int(number) <= 25, "questionCount": 50 if 1 <= int(number) <= 25 else 0},
        "lastOfflineValidated": "2026-09-02", "lastLiveVerified": None,
    }


INTEGER_INPUTS = {
    "ApprovedBitsPerSecond", "ApprovedReplicaCount", "ApprovedShortTermRetentionDays",
    "ApprovedVCoreCeiling", "RequiredRetentionDays",
}
BOOLEAN_INPUTS = {
    "ApprovedFirewallEgressRoute", "ConflictResolutionProcedureApproved", "RequirePrivateAccess",
}


def env_name(name: str) -> str:
    """Return the explicit AZ305 environment fallback for a public input."""
    snake = re.sub(r"(?<!^)(?=[A-Z])", "_", name).upper()
    return f"AZ305_{snake}"


def input_declaration(name: str) -> str:
    fallback = env_name(name)
    if name in INTEGER_INPUTS:
        return f"[int]${name} = $(if ($env:{fallback}) {{ [int]$env:{fallback} }} else {{ 0 }})"
    if name in BOOLEAN_INPUTS:
        return (
            f"[bool]${name} = $(if ($env:{fallback}) {{ "
            f"[System.Convert]::ToBoolean($env:{fallback}) }} else {{ $false }})"
        )
    return f"[string]${name} = $env:{fallback}"


def discover_inputs_for_fields(content: dict[str, Any], fields: tuple[str, ...]) -> list[str]:
    source = "\n".join(
        str(checkpoint.get(field, ""))
        for checkpoint in content["checkpoints"]
        for field in fields
    )
    names = set(re.findall(r"(?<!\$)\$([A-Za-z_][A-Za-z0-9_]*)", source))
    assigned = set(re.findall(r"\$([A-Za-z_][A-Za-z0-9_]*)\s*=", source))
    assigned.update(re.findall(r"(?i)foreach\s*\(\s*\$([A-Za-z_][A-Za-z0-9_]*)\s+in\b", source))
    names.difference_update(assigned)
    excluded = {
        "SubscriptionId", "TenantId", "RunId", "Location", "SecondaryLocation", "ResourceGroup", "WorkloadName",
        "Execute", "AcknowledgeCost", "AcknowledgeTenantChange", "ExpiresOn", "true", "false", "null", "env",
        "PSVersionTable", "PSScriptRoot", "ErrorActionPreference", "LASTEXITCODE", "_", "input", "args", "matches",
    }
    return sorted(name for name in names if name not in excluded)


def command_uses_native(command: str) -> bool:
    return re.search(r"(?i)(?<![A-Za-z0-9_.-])(?:az|azcopy|bicep)(?:\.cmd|\.exe)?\b", command) is not None


def command_uses_cloud(command: str, track: str) -> bool:
    if track == "azure-cli":
        without_local_bicep = re.sub(r"(?i)(?<![A-Za-z0-9_.-])az\s+bicep\s+build\b", "", command)
        return bool(re.search(r"(?i)(?<![A-Za-z0-9_.-])(?:az|azcopy)(?:\.cmd|\.exe)?\b", without_local_bicep))
    if track == "azure-powershell":
        return bool(re.search(r"\b(?:Get|New|Set|Remove|Update|Test|Invoke|Start|Stop|Enable|Disable)-(?:Az|Mg)[A-Za-z0-9.]*\b", command, re.IGNORECASE))
    return False


def mutation_kind(command: str) -> Optional[str]:
    normalized = command.strip()
    folded = f" {normalized.casefold()} "
    if " what-if " in folded or " -whatif " in folded or " --dry-run " in folded:
        return None
    if (
        " create " in folded
        or re.search(r"(?i)(?:^|[;|]\s*)(?:New|Add)-Az[A-Za-z0-9.]*\b", normalized)
        or re.search(r"(?i)(?:^|[;|]\s*)New-Mg[A-Za-z0-9.]*\b", normalized)
        or re.search(r"(?i)\baz\s+deployment\s+(?:group|sub|mg|tenant)\s+create\b", normalized)
    ):
        return "create"
    if (
        any(token in folded for token in (" update ", " set ", " assign ", " add ", " enable ", " migrate "))
        or re.search(r"(?i)(?:^|[;|]\s*)(?:Set|Update)-Az[A-Za-z0-9.]*\b", normalized)
        or re.search(r"(?i)(?:^|[;|]\s*)Update-Mg[A-Za-z0-9.]*\b", normalized)
    ):
        return "change"
    return None


def is_deployment_create(command: str) -> bool:
    return bool(re.search(r"(?i)\baz\s+deployment\s+(?:group|sub|mg|tenant)\s+create\b", command))


def is_deployment_what_if(command: str) -> bool:
    return bool(re.search(r"(?i)\baz\s+deployment\s+(?:group|sub|mg|tenant)\s+what-if\b", command))


def command_has_ownership(command: str) -> bool:
    folded = command.casefold()
    return (
        all(token in folded for token in ("purpose", "az305-lab", "labid", "runid", "expireson"))
        or "artifacts/main.bicep" in folded
    )


def referenced_id_variables(command: str) -> list[str]:
    return sorted(set(re.findall(r"\$([A-Za-z_][A-Za-z0-9_]*(?:ResourceId|DcrId))\b", command)))


def common_parameters(lab: dict[str, Any], content: dict[str, Any], extra: Optional[list[str]] = None) -> str:
    parameters = [
        "    [string]$SubscriptionId = $env:AZ305_SUBSCRIPTION_ID",
        "    [string]$TenantId = $env:AZ305_TENANT_ID",
        "    [ValidatePattern('^[a-z0-9-]{6,64}$')][string]$RunId = $env:AZ305_RUN_ID",
        "    [string]$Location = $(if ($env:AZ305_LOCATION) { $env:AZ305_LOCATION } else { 'westeurope' })",
        "    [string]$SecondaryLocation = $(if ($env:AZ305_SECONDARY_LOCATION) { $env:AZ305_SECONDARY_LOCATION } else { 'northeurope' })",
        "    [string]$ResourceGroup = $(if ($env:AZ305_RESOURCE_GROUP) { $env:AZ305_RESOURCE_GROUP } else { \"rg-az305-$RunId\" })",
        "    [string]$WorkloadName = $(if ($env:AZ305_WORKLOAD_NAME) { $env:AZ305_WORKLOAD_NAME } else { \"az305-$RunId\" })",
        "    [string]$ExpiresOn = $(if ($env:AZ305_EXPIRES_ON) { $env:AZ305_EXPIRES_ON } else { (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd') })",
    ]
    for name in discover_inputs(content):
        parameters.append(f"    {input_declaration(name)}")
    parameters.extend(extra or [])
    parameters.extend(["    [switch]$Execute", "    [switch]$AcknowledgeCost", "    [switch]$AcknowledgeTenantChange"])
    parameter_names = ["SubscriptionId", "TenantId", "RunId", "Location", "SecondaryLocation", "ResourceGroup", "WorkloadName", "ExpiresOn", *discover_inputs(content)]
    if extra:
        for declaration in extra:
            match = re.search(r"\$([A-Za-z_][A-Za-z0-9_]*)", declaration)
            if match:
                parameter_names.append(match.group(1))
    parameter_names.extend(["Execute", "AcknowledgeCost", "AcknowledgeTenantChange"])
    use_contract = "@(" + ", ".join(f"${name}" for name in parameter_names) + ") | Out-Null"
    return "[CmdletBinding()]\nparam(\n" + ",\n".join(parameters) + "\n)\n\n$ErrorActionPreference = 'Stop'\n$PSNativeCommandUseErrorActionPreference = $true\nif (-not $RunId) { [Console]::Error.WriteLine('RunId or AZ305_RUN_ID is required.'); exit 2 }\n# Every lifecycle entrypoint intentionally exposes the same public parameter contract.\n" + use_contract + "\n"


def required_inputs_block(names: list[str]) -> str:
    if not names:
        return "# This execution path has no additional required lab input."
    entries = "; ".join(f"{name} = ${name}" for name in names)
    return f"""$requiredLabInputs = [ordered]@{{ {entries} }}
$missingLabInputs = @($requiredLabInputs.GetEnumerator() | Where-Object {{ $_.Value -is [string] -and [string]::IsNullOrWhiteSpace([string]$_.Value) }} | ForEach-Object Key)
if ($missingLabInputs.Count -gt 0) {{ [Console]::Error.WriteLine("Execution is gated; supply: $($missingLabInputs -join ', ')."); exit 2 }}"""


def required_executables(lab: dict[str, Any], content: dict[str, Any]) -> list[str]:
    corpus = "\n".join(
        str(checkpoint.get(field, ""))
        for checkpoint in content["checkpoints"]
        for field in ("command", "positiveCommand", "negativeCommand")
    )
    required = {"pwsh"}
    if re.search(r"(?i)(?<![A-Za-z0-9_.-])az(?:\.cmd|\.exe)?\b", corpus):
        required.add("az")
    if re.search(r"(?i)(?<![A-Za-z0-9_.-])azcopy(?:\.exe)?\b", corpus):
        required.add("azcopy")
    if re.search(r"(?i)(?<![A-Za-z0-9_.-])bicep(?:\.exe)?\s+build\b", corpus):
        required.add("bicep")
    return sorted(required)


def preflight_script(lab: dict[str, Any], content: dict[str, Any]) -> str:
    required = "@(" + ", ".join(ps_single(item) for item in required_executables(lab, content)) + ")"
    command_corpus = "\n".join(
        str(checkpoint.get(field, ""))
        for checkpoint in content["checkpoints"]
        for field in ("command", "positiveCommand", "negativeCommand")
    )
    cmdlets = sorted(set(re.findall(
        r"\b(?:Get|New|Set|Remove|Update|Test|Invoke|Start|Stop|Enable|Disable)-(?:Az|Mg)[A-Za-z0-9.]*\b",
        command_corpus,
        re.IGNORECASE,
    )))
    cmdlet_check = ""
    if cmdlets:
        names = "@(" + ", ".join(ps_single(item) for item in cmdlets) + ")"
        cmdlet_check = f"""
$requiredCmdlets = {names}
$missingCmdlets = @($requiredCmdlets | Where-Object {{ -not (Get-Command $_ -ErrorAction SilentlyContinue) }})
if ($missingCmdlets.Count -gt 0) {{
    Write-Error "Missing local cmdlets: $($missingCmdlets -join ', ')"
    exit 1
}}"""
    graph_check = "\nif (Get-Module -ListAvailable -Name 'Microsoft.Graph.Beta*') { throw 'Microsoft.Graph Beta modules are not permitted.' }" if lab.get("graphPowerShell") else ""
    return common_parameters(lab, content) + f"""
$requiredCommands = {required}
$missing = @($requiredCommands | Where-Object {{ -not (Get-Command $_ -ErrorAction SilentlyContinue) }})
if ($missing.Count -gt 0) {{
    Write-Error "Missing local commands: $($missing -join ', ')"
    exit 1
}}{cmdlet_check}{graph_check}

[pscustomobject]@{{
    labId = '{lab['id']}'
    track = '{lab['track']}'
    implementationMode = '{lab['implementationMode']}'
    result = 'pass'
    note = 'Local tool discovery only; no Azure or Microsoft Graph request was made.'
}} | ConvertTo-Json
exit 0
"""


def context_flags(lab: dict[str, Any], corpus: str, force_azure: bool = False) -> tuple[bool, bool, bool]:
    cli = lab["track"] == "azure-cli" and (force_azure or command_uses_cloud(corpus, "azure-cli"))
    az_power_shell = lab["track"] == "azure-powershell" and (
        force_azure or bool(re.search(r"\b(?:Get|New|Set|Remove|Update|Test|Invoke|Start|Stop|Enable|Disable)-Az[A-Za-z0-9.]*\b", corpus, re.IGNORECASE))
    )
    graph = lab["track"] == "azure-powershell" and bool(re.search(
        r"\b(?:Get|New|Set|Remove|Update|Test|Invoke|Start|Stop|Enable|Disable)-Mg[A-Za-z0-9.]*\b",
        corpus,
        re.IGNORECASE,
    ))
    return cli, az_power_shell, graph


def context_helpers(lab: dict[str, Any], corpus: str, force_azure: bool = False) -> tuple[str, str]:
    cli, az_power_shell, graph = context_flags(lab, corpus, force_azure)
    if cli:
        helper = r"""
function Invoke-AzCliJson {
    [CmdletBinding()]
    param([Parameter(Mandatory)][string[]]$ArgumentList)
    $savedNativePreference = $PSNativeCommandUseErrorActionPreference
    try {
        # Capture the exit code ourselves so a failed native command cannot be
        # mistaken for an empty but successful JSON response.
        $PSNativeCommandUseErrorActionPreference = $false
        $outputLines = @(& az @ArgumentList)
        $nativeExit = $LASTEXITCODE
    }
    finally {
        $PSNativeCommandUseErrorActionPreference = $savedNativePreference
    }
    if ($nativeExit -ne 0) { throw "Azure CLI exited with code $nativeExit." }
    $raw = @($outputLines) -join "`n"
    if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
    try { return ($raw | ConvertFrom-Json -Depth 100) }
    catch { throw 'Azure CLI returned data that was not valid JSON.' }
}

function Assert-ExactExecutionContext {
    [CmdletBinding()]
    param([string]$ExpectedSubscriptionId, [string]$ExpectedTenantId)
    if ([string]::IsNullOrWhiteSpace($ExpectedSubscriptionId) -or [string]::IsNullOrWhiteSpace($ExpectedTenantId)) {
        throw 'SubscriptionId and TenantId are required before a cloud request.'
    }
    $context = Invoke-AzCliJson -ArgumentList @('account', 'show', '--output', 'json', '--only-show-errors')
    if (-not $context -or [string]$context.id -ine $ExpectedSubscriptionId -or [string]$context.tenantId -ine $ExpectedTenantId) {
        throw 'The active Azure CLI subscription or tenant does not exactly match the requested context.'
    }
}
"""
        return helper, "Assert-ExactExecutionContext -ExpectedSubscriptionId $SubscriptionId -ExpectedTenantId $TenantId"
    if az_power_shell or graph:
        checks: list[str] = []
        if graph and not az_power_shell:
            checks.append("    # SubscriptionId remains part of the uniform lifecycle contract; Graph context is tenant-scoped.\n    $null = $ExpectedSubscriptionId")
        if az_power_shell:
            checks.append(r"""    if ([string]::IsNullOrWhiteSpace($ExpectedSubscriptionId) -or [string]::IsNullOrWhiteSpace($ExpectedTenantId)) { throw 'SubscriptionId and TenantId are required before an Azure request.' }
    $azContext = Get-AzContext -ErrorAction Stop
    if (-not $azContext -or [string]$azContext.Subscription.Id -ine $ExpectedSubscriptionId -or [string]$azContext.Tenant.Id -ine $ExpectedTenantId) {
        throw 'The active Azure PowerShell subscription or tenant does not exactly match the requested context.'
    }""")
        if graph:
            checks.append(r"""    if ([string]::IsNullOrWhiteSpace($ExpectedTenantId)) { throw 'TenantId is required before a Microsoft Graph request.' }
    $graphContext = Get-MgContext -ErrorAction Stop
    if (-not $graphContext -or [string]$graphContext.TenantId -ine $ExpectedTenantId) {
        throw 'The active Microsoft Graph tenant does not exactly match the requested tenant.'
    }""")
        helper = """
function Assert-ExactExecutionContext {
    [CmdletBinding()]
    param([string]$ExpectedSubscriptionId, [string]$ExpectedTenantId)
%s
}
""" % "\n".join(checks)
        return helper, "Assert-ExactExecutionContext -ExpectedSubscriptionId $SubscriptionId -ExpectedTenantId $TenantId"
    return "", "# This offline-only execution path requires no authenticated context."


def native_exit_guard(command: str, label: str, indent: str = "    ") -> str:
    if not command_uses_native(command):
        return ""
    return f"{indent}if ($LASTEXITCODE -ne 0) {{ throw '{label} native command exited with code ' + $LASTEXITCODE + '.' }}\n"


def setup_script(lab: dict[str, Any], content: dict[str, Any]) -> str:
    cost_gate = content["costClass"] in {"moderate", "elevated", "medium"}
    tenant_gate = bool(lab.get("graphPowerShell"))
    setup_corpus = "\n".join(str(cp["command"]) for cp in content["checkpoints"])
    context_definition, context_call = context_helpers(lab, setup_corpus)
    design_cloud_gate = lab["implementationMode"] == "design-simulation" and command_uses_cloud(setup_corpus, lab["track"])
    foundation_preview = lab["id"] == "LAB-00"
    lab_inputs = discover_inputs(content)
    required_setup_inputs = discover_inputs_for_fields(content, ("command",))
    input_entries = [
        "subscriptionId = $SubscriptionId", "tenantId = $TenantId", "location = $Location",
        "secondaryLocation = $SecondaryLocation", "resourceGroup = $ResourceGroup",
        "workloadName = $WorkloadName", "expiresOn = $ExpiresOn",
        *(f"{name} = ${name}" for name in lab_inputs),
    ]
    commands = []
    deployment_create_indexes = {
        index for index, checkpoint in enumerate(content["checkpoints"], 1)
        if is_deployment_create(str(checkpoint["command"]))
    }
    for index, cp in enumerate(content["checkpoints"], 1):
        command = str(cp["command"]).strip()
        kind = mutation_kind(command)
        ownership = command_has_ownership(command)
        targets = referenced_id_variables(command)
        before_parts: list[str] = []
        if kind:
            target_array = "@(" + ", ".join(f"${name}" for name in targets) + ")"
            before_parts.append(
                f"    Assert-ManagedMutation -State $state -CheckpointId 'LAB{lab['number']}-CP0{index}' "
                f"-CarriesOwnership:${str(ownership).lower()} -TargetResourceIds {target_array}\n"
            )
        if kind == "change":
            positive = str(cp.get("positiveCommand", "")).strip()
            if positive:
                target_array = "@(" + ", ".join(f"${name}" for name in targets) + ")"
                setting_label = ps_single(f"LAB{lab['number']}-CP0{index}: {cp['title']}")
                before_parts.append(f"""    # Capture the original non-secret projection before changing an exact run-owned object.
    $originalProjection = & {{ {positive} }}
{native_exit_guard(positive, f'LAB{lab["number"]}-CP0{index} original-state', '    ')}    Assert-SafeStateValue -Value $originalProjection
    foreach ($originalTargetId in {target_array}) {{
        $state.originalSettings += [pscustomobject]@{{ id = $originalTargetId; setting = {setting_label}; value = $originalProjection }}
    }}
    Save-RunState -State $state
""")
        record = ""
        if is_deployment_what_if(command) and any(later > index for later in deployment_create_indexes):
            record += f"""    # Persist exact what-if resource IDs as recovery locators before the later deployment mutation.
    $plannedCandidate = Convert-CheckpointOutput -Value $stepResult
    $plannedIds = @(Get-PlannedDeploymentResourceId -Value $plannedCandidate)
    if ($plannedIds.Count -eq 0) {{ throw 'LAB{lab['number']}-CP0{index} returned no exact planned ARM resource ID for partial-failure recovery.' }}
    foreach ($plannedId in $plannedIds) {{
        if ($plannedId -notmatch '^/subscriptions/([^/]+)/' -or $Matches[1] -ine $SubscriptionId) {{ throw 'A planned recovery ID belongs to a different subscription.' }}
        if (@($state.managedObjects | Where-Object {{ $_.id -ieq $plannedId }}).Count -eq 0) {{
            $state.managedObjects += [pscustomobject]@{{
                id = $plannedId
                type = 'planned-azure-resource'
                tags = [ordered]@{{ purpose = 'az305-lab'; labId = '{lab['id']}'; runId = $RunId; expiresOn = $ExpiresOn }}
            }}
            Save-RunState -State $state
        }}
    }}
"""
        if kind == "create" and ownership:
            record += f"""    $candidate = Convert-CheckpointOutput -Value $stepResult
    $returnedIds = @(Get-ReturnedResourceId -Value $candidate)
    if ($returnedIds.Count -eq 0) {{ throw 'LAB{lab['number']}-CP0{index} created an owned resource but returned no recoverable ARM resource ID.' }}
    foreach ($returnedId in $returnedIds) {{
        if ($returnedId -notmatch '^/subscriptions/([^/]+)/' -or $Matches[1] -ine $SubscriptionId) {{ throw 'A returned recovery ID belongs to a different subscription.' }}
        if (@($state.managedObjects | Where-Object {{ $_.id -ieq $returnedId }}).Count -eq 0) {{
            $state.managedObjects += [pscustomobject]@{{
                id = $returnedId
                type = 'azure-resource'
                tags = [ordered]@{{ purpose = 'az305-lab'; labId = '{lab['id']}'; runId = $RunId; expiresOn = $ExpiresOn }}
            }}
            Save-RunState -State $state
        }}
    }}
"""
        commands.append(f"""    # {lab['number']}-CP0{index}: {cp['title']}
{''.join(before_parts)}    $stepResult = & {{ {command} }}
{native_exit_guard(command, f'LAB{lab["number"]}-CP0{index}', '    ')}{record}    $null = $stepResult
""")
    command_block = "\n".join(commands)
    planning_only = lab["implementationMode"] == "design-simulation" or lab["id"] in {"LAB-21", "LAB-26"}
    status_transition = (
        "# Planning-only execution remains initialized until its bounded checks complete."
        if planning_only
        else "$state.status = 'deploying'\nSave-RunState -State $state"
    )
    completed_status = "planned" if planning_only else "deployed"
    return common_parameters(lab, content) + f"""
$LabRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$StateRoot = Join-Path $LabRoot ".state/$RunId"
$StatePath = Join-Path $StateRoot 'run.json'
{context_definition}
function Save-RunState {{
    [CmdletBinding()]
    param([Parameter(Mandatory)]$State)
    $temporaryPath = "$StatePath.tmp"
    $State | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $temporaryPath -Encoding utf8NoBOM
    Move-Item -LiteralPath $temporaryPath -Destination $StatePath -Force
}}

function Assert-SafeStateValue {{
    [CmdletBinding()]
    param($Value)
    $serialized = $Value | ConvertTo-Json -Depth 12 -Compress
    if ($serialized -match '(?i)"(?:token|password|secret|certificate|connectionString|sas|clientSecret|accessToken|refreshToken|accountKey|privateKey)"\\s*:') {{
        throw 'A prohibited sensitive field name was returned; state capture is refused.'
    }}
}}

function Convert-CheckpointOutput {{
    [CmdletBinding()]
    param($Value)
    if ($Value -is [string]) {{ $raw = [string]$Value }}
    elseif ($Value -is [System.Collections.IEnumerable] -and @($Value | Where-Object {{ $_ -isnot [string] }}).Count -eq 0) {{ $raw = @($Value) -join "`n" }}
    else {{ return $Value }}
    if ([string]::IsNullOrWhiteSpace($raw)) {{ return $null }}
    try {{ return ($raw | ConvertFrom-Json -Depth 100) }} catch {{ return $Value }}
}}

function Get-ReturnedResourceId {{
    [CmdletBinding()]
    param($Value)
    $seen = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $results = [System.Collections.Generic.List[string]]::new()
    function Add-ArmId {{
        param($Candidate)
        if ($Candidate -is [string] -and $Candidate -match '^/subscriptions/[0-9a-f-]+/(?:resourceGroups/[^/]+(?:/providers/.+)?|providers/.+)$' -and $Candidate -notmatch '/providers/Microsoft\\.Resources/deployments/') {{
            if ($seen.Add($Candidate)) {{ $results.Add($Candidate) }}
        }}
    }}
    function Find-DeploymentOutputId {{
        param($Item, [int]$Depth)
        if ($null -eq $Item -or $Depth -gt 12) {{ return }}
        if ($Item -is [string]) {{ Add-ArmId -Candidate $Item; return }}
        if ($Item -is [System.Collections.IDictionary]) {{ foreach ($key in $Item.Keys) {{ Find-DeploymentOutputId -Item $Item[$key] -Depth ($Depth + 1) }}; return }}
        if ($Item -is [System.Collections.IEnumerable]) {{ foreach ($entry in $Item) {{ Find-DeploymentOutputId -Item $entry -Depth ($Depth + 1) }}; return }}
        foreach ($property in @($Item.PSObject.Properties | Where-Object {{ $_.MemberType -in @('NoteProperty', 'Property') }})) {{ Find-DeploymentOutputId -Item $property.Value -Depth ($Depth + 1) }}
    }}
    foreach ($rootItem in @($Value)) {{
        if ($rootItem -is [System.Collections.IDictionary]) {{
            foreach ($name in @('id', 'resourceId')) {{ if ($rootItem.Contains($name)) {{ Add-ArmId -Candidate $rootItem[$name] }} }}
            if ($rootItem.Contains('properties') -and $rootItem.properties -and $rootItem.properties.outputs) {{ Find-DeploymentOutputId -Item $rootItem.properties.outputs -Depth 0 }}
            continue
        }}
        foreach ($name in @('Id', 'ResourceId')) {{
            $property = $rootItem.PSObject.Properties[$name]
            if ($property) {{ Add-ArmId -Candidate $property.Value }}
        }}
        if ($rootItem.PSObject.Properties['Properties'] -and $rootItem.Properties -and $rootItem.Properties.outputs) {{
            Find-DeploymentOutputId -Item $rootItem.Properties.outputs -Depth 0
        }}
    }}
    return @($results)
}}

function Get-PlannedDeploymentResourceId {{
    [CmdletBinding()]
    param($Value)
    $seen = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $results = [System.Collections.Generic.List[string]]::new()
    foreach ($change in @($Value.changes)) {{
        $candidate = [string]$change.resourceId
        if ($candidate -match '^/subscriptions/[0-9a-f-]+/(?:resourceGroups/[^/]+(?:/providers/.+)?|providers/.+)$' -and $candidate -notmatch '/providers/Microsoft\\.Resources/deployments/' -and $seen.Add($candidate)) {{
            $results.Add($candidate)
        }}
    }}
    return @($results)
}}

function Assert-InputSubscriptionScope {{
    [CmdletBinding()]
    param($Inputs, [string]$ExpectedSubscriptionId)
    $entries = if ($Inputs -is [System.Collections.IDictionary]) {{
        @($Inputs.GetEnumerator())
    }} else {{
        @($Inputs.PSObject.Properties | ForEach-Object {{ [pscustomobject]@{{ Key = $_.Name; Value = $_.Value }} }})
    }}
    foreach ($entry in $entries) {{
        if ($entry.Value -is [string] -and [string]$entry.Value -match '^/subscriptions/([^/]+)/') {{
            if ($Matches[1] -ine $ExpectedSubscriptionId) {{ throw "Input $($entry.Key) belongs to a different subscription." }}
        }}
    }}
}}

function Assert-ManagedMutation {{
    [CmdletBinding()]
    param($State, [string]$CheckpointId, [bool]$CarriesOwnership, [object[]]$TargetResourceIds)
    if ($CarriesOwnership) {{ return }}
    $targets = @($TargetResourceIds | Where-Object {{ $_ -is [string] -and $_ -match '^/subscriptions/' }})
    if ($targets.Count -eq 0) {{ throw "$CheckpointId refuses an untagged mutation because no exact ARM target ID was supplied." }}
    $knownIds = @($State.managedObjects | ForEach-Object {{ [string]$_.id }})
    if ($knownIds.Count -eq 0) {{ throw "$CheckpointId refuses to modify a pre-existing object because no run-owned parent has been recorded." }}
    foreach ($target in $targets) {{
        $related = @($knownIds | Where-Object {{ $target -ieq $_ -or $target.StartsWith("$_/", [System.StringComparison]::OrdinalIgnoreCase) -or $_.StartsWith("$target/", [System.StringComparison]::OrdinalIgnoreCase) }}).Count -gt 0
        if (-not $related) {{ throw "$CheckpointId refuses a mutation outside the exact run-owned resource boundary." }}
    }}
}}

$executionInputs = [ordered]@{{ {'; '.join(input_entries)} }}
{(f'''if (-not $Execute) {{
    if (Test-Path -LiteralPath $StatePath) {{ [Console]::Error.WriteLine('Run state already exists; the intent record will not be overwritten.'); exit 2 }}
    Assert-SafeStateValue -Value $executionInputs
    New-Item -ItemType Directory -Path $StateRoot -Force | Out-Null
    $state = [ordered]@{{
        schemaVersion = '1.0.0'; labId = '{lab['id']}'; runId = $RunId; track = '{lab['track']}'
        implementationMode = '{lab['implementationMode']}'; status = 'planned'
        createdAt = (Get-Date).ToUniversalTime().ToString('o'); execute = $false
        parameters = $executionInputs; managedObjects = @(); originalSettings = @()
    }}
    Save-RunState -State $state
    Write-Output '[preview] Offline intent state was written; no authentication or cloud command was used.'
    exit 0
}}''' if foundation_preview else '')}
if (-not $Execute) {{
    Write-Output '[preview] No cloud command was called and no state was created.'
    Write-Output '[preview] Re-run with -Execute only in an authorized disposable environment.'
    exit 0
}}
{("[Console]::Error.WriteLine('This design-simulation setup is offline-only and refuses its authored cloud commands.'); exit 2" if design_cloud_gate else "# This setup is compatible with the lab implementation mode.")}
{("if (-not $AcknowledgeCost) { [Console]::Error.WriteLine('Cost acknowledgement is required.'); exit 2 }" if cost_gate else "# This default exercise does not require a cost acknowledgement.")}
{("if (-not $AcknowledgeTenantChange) { [Console]::Error.WriteLine('Tenant-change acknowledgement is required.'); exit 2 }" if tenant_gate else "# This lab does not perform a tenant-scoped change by default.")}
{required_inputs_block(required_setup_inputs)}

try {{
    {context_call}
    Assert-InputSubscriptionScope -Inputs $executionInputs -ExpectedSubscriptionId $SubscriptionId
    Assert-SafeStateValue -Value $executionInputs
}}
catch {{
    [Console]::Error.WriteLine("Execution is gated by context or input validation: $($_.Exception.Message)")
    exit 2
}}

# Recovery state is persisted before the first possible mutation below.
if (Test-Path -LiteralPath $StatePath) {{
    [Console]::Error.WriteLine('Run state already exists. Choose a new RunId or complete the recorded cleanup; existing recovery state will not be overwritten.')
    exit 2
}}
New-Item -ItemType Directory -Path $StateRoot -Force | Out-Null
$state = [ordered]@{{
    schemaVersion = '1.0.0'; labId = '{lab['id']}'; runId = $RunId; track = '{lab['track']}'
    implementationMode = '{lab['implementationMode']}'; status = 'initialized'
    createdAt = (Get-Date).ToUniversalTime().ToString('o'); execute = $true
    parameters = $executionInputs
    managedObjects = @(); originalSettings = @()
}}
Save-RunState -State $state
{status_transition}

$originalLocation = Get-Location
try {{
    Set-Location -LiteralPath $LabRoot
{command_block}
    $state.status = '{completed_status}'
    Save-RunState -State $state
}} catch {{
    $state.status = 'failed'
    Save-RunState -State $state
    Write-Error $_
    exit 1
}} finally {{
    Set-Location -LiteralPath $originalLocation
}}
exit 0
"""


def validate_script(lab: dict[str, Any], content: dict[str, Any]) -> str:
    number = lab["number"]
    validation_corpus = "\n".join(
        str(cp.get(field, ""))
        for cp in content["checkpoints"]
        for field in ("positiveCommand", "negativeCommand")
    )
    context_definition, context_call = context_helpers(lab, validation_corpus)
    validation_uses_cloud = command_uses_cloud(validation_corpus, lab["track"])
    required_validation_inputs = discover_inputs_for_fields(content, ("positiveCommand", "negativeCommand"))
    if required_validation_inputs:
        entries = "; ".join(f"{name} = ${name}" for name in required_validation_inputs)
        required_block = f"""$requiredValidationInputs = [ordered]@{{ {entries} }}
$missingValidationInputs = @($requiredValidationInputs.GetEnumerator() | Where-Object {{ $_.Value -is [string] -and [string]::IsNullOrWhiteSpace([string]$_.Value) }} | ForEach-Object Key)"""
    else:
        required_block = "$missingValidationInputs = @()"
    checkpoint_assertions: list[str] = []
    for index, cp in enumerate(content["checkpoints"], 1):
        positive = str(cp.get("positiveCommand", "")).strip()
        negative = str(cp.get("negativeCommand", "")).strip()
        positive_self_asserting = "throw " in positive.casefold() or "exit 1" in positive.casefold()
        negative_self_asserting = "throw " in negative.casefold() or "exit 1" in negative.casefold()
        positive_evaluation = "$true" if positive_self_asserting else "(Test-PositiveEvidence -Value $positiveEvidence)"
        negative_evaluation = "$true" if negative_self_asserting else "(Test-NegativeEvidence -Value $negativeEvidence)"
        checkpoint_assertions.append(f"""# LAB{number}-CP0{index}: run both polarities even when one fails.
$positivePassed = $false
try {{
    $global:LASTEXITCODE = 0
    $positiveEvidence = & {{ {positive} }}
{native_exit_guard(positive, f'LAB{number}-CP0{index} positive', '    ')}    $positivePassed = {positive_evaluation}
    $null = $positiveEvidence
}} catch {{ $positivePassed = $false }}
Add-ValidationAssertion -Id 'LAB{number}-CP0{index}-POS' -Kind positive -Passed $positivePassed -Message {ps_single(cp['expected'])}

$negativePassed = $false
try {{
    $global:LASTEXITCODE = 0
    $negativeEvidence = & {{ {negative} }}
{native_exit_guard(negative, f'LAB{number}-CP0{index} negative', '    ')}    $negativePassed = {negative_evaluation}
    $null = $negativeEvidence
}} catch {{ $negativePassed = $false }}
Add-ValidationAssertion -Id 'LAB{number}-CP0{index}-NEG' -Kind negative -Passed $negativePassed -Message {ps_single(cp['negative'])}
""")
    checkpoint_block = "\n".join(checkpoint_assertions)
    design_cloud_gate = lab["implementationMode"] == "design-simulation" and command_uses_cloud(validation_corpus, lab["track"])
    return common_parameters(lab, content, ["    [ValidateSet('Deployment', 'PostCleanup')][string]$Mode = 'Deployment'"]) + f"""
$LabRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$StateRoot = Join-Path $LabRoot ".state/$RunId"
$RunPath = Join-Path $StateRoot 'run.json'
$ValidationPath = Join-Path $StateRoot 'validation.json'
{context_definition}

if (-not (Test-Path -LiteralPath $RunPath)) {{
    Write-Warning 'No run state exists; validation is gated.'
    exit 2
}}
$state = Get-Content -LiteralPath $RunPath -Raw | ConvertFrom-Json
$assertions = [System.Collections.Generic.List[object]]::new()
function Add-ValidationAssertion {{
    [CmdletBinding()]
    param([string]$Id, [ValidateSet('positive', 'negative')][string]$Kind, [bool]$Passed, [string]$Message)
    $assertions.Add([pscustomobject]@{{ id = $Id; kind = $Kind; passed = $Passed; message = $Message }})
}}

function Save-ValidationArtifact {{
    [CmdletBinding()]
    param([ValidateSet('pass', 'partial', 'fail')][string]$Result)
    $artifact = [ordered]@{{ schemaVersion = '1.0.0'; labId = '{lab['id']}'; runId = $RunId; mode = $Mode; result = $Result; validatedAt = (Get-Date).ToUniversalTime().ToString('o'); assertions = @($assertions) }}
    $artifact | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $ValidationPath -Encoding utf8NoBOM
}}

function Test-PositiveEvidence {{
    [CmdletBinding()]
    param($Value)
    if ($Value -is [bool]) {{ return $Value }}
    if ($null -eq $Value) {{ return $false }}
    if ($Value -is [string]) {{ return -not [string]::IsNullOrWhiteSpace($Value) }}
    if ($Value -is [System.Collections.IEnumerable]) {{ return @($Value).Count -gt 0 }}
    return $true
}}

function Test-NegativeEvidence {{
    [CmdletBinding()]
    param($Value)
    if ($Value -is [bool]) {{ return $Value }}
    if ($null -eq $Value) {{ return $true }}
    if ($Value -is [string]) {{ return [string]::IsNullOrWhiteSpace($Value) }}
    if ($Value -is [System.Collections.IEnumerable]) {{ return @($Value).Count -eq 0 }}
    $properties = @($Value.PSObject.Properties | Where-Object {{ $_.MemberType -in @('NoteProperty', 'Property') }})
    if ($properties.Count -eq 0) {{ return $false }}
    return @($properties | Where-Object {{ -not (Test-NegativeEvidence -Value $_.Value) }}).Count -eq 0
}}

function Test-ProhibitedStateField {{
    [CmdletBinding()]
    param($Value)
    $serialized = $Value | ConvertTo-Json -Depth 20
    return $serialized -match '(?i)"(?:token|password|secret|certificate|connectionString|sas|clientSecret|accessToken|refreshToken|accountKey|privateKey)"\\s*:'
}}

function Assert-InputSubscriptionScope {{
    [CmdletBinding()]
    param($Inputs, [string]$ExpectedSubscriptionId)
    $entries = if ($Inputs -is [System.Collections.IDictionary]) {{
        @($Inputs.GetEnumerator())
    }} else {{
        @($Inputs.PSObject.Properties | ForEach-Object {{ [pscustomobject]@{{ Key = $_.Name; Value = $_.Value }} }})
    }}
    foreach ($entry in $entries) {{
        if ($entry.Value -is [string] -and [string]$entry.Value -match '^/subscriptions/([^/]+)/' -and $Matches[1] -ine $ExpectedSubscriptionId) {{
            throw "Input $($entry.Key) belongs to a different subscription."
        }}
    }}
}}

$stateIdentityMatches = (
    $state.labId -ceq '{lab['id']}' -and
    $state.runId -ceq $RunId -and
    $state.track -ceq '{lab['track']}' -and
    $state.implementationMode -ceq '{lab['implementationMode']}' -and
    {("([string]$state.parameters.subscriptionId -ieq $SubscriptionId -and [string]$state.parameters.tenantId -ieq $TenantId)" if validation_uses_cloud else "$true")}
)
Add-ValidationAssertion -Id 'LAB{number}-VAL-POS-01' -Kind positive -Passed $stateIdentityMatches -Message 'Run identity, implementation mode, command track, tenant, and subscription exactly match the copied lab and requested run.'
$hasSensitiveName = Test-ProhibitedStateField -Value $state
Add-ValidationAssertion -Id 'LAB{number}-VAL-NEG-01' -Kind negative -Passed (-not $hasSensitiveName) -Message 'State contains no prohibited sensitive field name.'

if ($Mode -eq 'PostCleanup') {{
    $cleanupPath = Join-Path $StateRoot 'cleanup.json'
    $cleanup = if (Test-Path -LiteralPath $cleanupPath) {{ Get-Content -LiteralPath $cleanupPath -Raw | ConvertFrom-Json }} else {{ $null }}
    Add-ValidationAssertion -Id 'LAB{number}-VAL-POS-02' -Kind positive -Passed ($null -ne $cleanup -and $cleanup.labId -ceq '{lab['id']}' -and $cleanup.runId -ceq $RunId -and $cleanup.result -eq 'pass' -and $cleanup.ownershipVerified) -Message 'The exact run cleanup completed with verified ownership.'
    Add-ValidationAssertion -Id 'LAB{number}-VAL-NEG-02' -Kind negative -Passed ($null -ne $cleanup -and $cleanup.activeManagedObjects -eq 0 -and @($state.managedObjects).Count -eq 0 -and @($state.originalSettings).Count -eq 0 -and $state.status -eq 'cleaned') -Message 'No active managed object or unresolved original setting remains in cleanup or run state.'
    $postCleanupPassed = @($assertions | Where-Object {{ -not $_.passed }}).Count -eq 0
    Save-ValidationArtifact -Result $(if ($postCleanupPassed) {{ 'pass' }} else {{ 'fail' }})
    if ($postCleanupPassed) {{ exit 0 }}
    exit 1
}}

Add-ValidationAssertion -Id 'LAB{number}-VAL-POS-02' -Kind positive -Passed {("($state.status -eq 'planned')" if lab['implementationMode'] == 'design-simulation' or lab['id'] in {'LAB-21', 'LAB-26'} else "($state.status -eq 'deployed')")} -Message '{("The planning-only setup completed and remains planned; no deployment is implied." if lab["implementationMode"] == "design-simulation" or lab["id"] in {"LAB-21", "LAB-26"} else "The executed setup completed successfully; a failed setup can never validate as pass.")}'
Add-ValidationAssertion -Id 'LAB{number}-VAL-NEG-02' -Kind negative -Passed (@($state.managedObjects | Where-Object {{ $_.tags.purpose -ne 'az305-lab' -or $_.tags.labId -ne '{lab['id']}' -or $_.tags.runId -ne $RunId }}).Count -eq 0) -Message 'No recorded object has a foreign ownership tag.'

if (@($assertions | Where-Object {{ -not $_.passed }}).Count -gt 0) {{
    Save-ValidationArtifact -Result 'fail'
    exit 1
}}
if (-not $Execute) {{
    {("if ($state.status -eq 'planned') { $offlinePassed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0; Save-ValidationArtifact -Result $(if ($offlinePassed) { 'pass' } else { 'fail' }); if ($offlinePassed) { exit 0 } else { exit 1 } }" if lab['id'] == 'LAB-00' else "# This lab has no special intent-only validation path.")}
    Save-ValidationArtifact -Result 'partial'
    Write-Warning 'Checkpoint validation is gated; re-run with -Execute after confirming the exact read-only context.'
    exit 2
}}
{("Save-ValidationArtifact -Result 'partial'; [Console]::Error.WriteLine('Design-simulation validation is offline-only and refuses cloud commands.'); exit 2" if design_cloud_gate else "# The validation surface is compatible with this lab implementation mode.")}
{required_block}
if ($missingValidationInputs.Count -gt 0) {{
    Add-ValidationAssertion -Id 'LAB{number}-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'One or more required non-secret validation inputs are missing.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}}
try {{
    {context_call}
    Assert-InputSubscriptionScope -Inputs $state.parameters -ExpectedSubscriptionId $SubscriptionId
    Add-ValidationAssertion -Id 'LAB{number}-VAL-POS-CONTEXT' -Kind positive -Passed $true -Message 'The active tenant and subscription exactly match the requested validation context.'
}}
catch {{
    Add-ValidationAssertion -Id 'LAB{number}-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'Exact execution context could not be proven.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}}

$originalLocation = Get-Location
try {{
    Set-Location -LiteralPath $LabRoot
{checkpoint_block}
}}
finally {{
    Set-Location -LiteralPath $originalLocation
}}

$passed = @($assertions | Where-Object {{ -not $_.passed }}).Count -eq 0
Save-ValidationArtifact -Result $(if ($passed) {{ 'pass' }} else {{ 'fail' }})
if ($passed) {{ exit 0 }}
exit 1
"""


def cleanup_script(lab: dict[str, Any], content: dict[str, Any]) -> str:
    cloud_cleanup = lab["track"] in {"azure-cli", "azure-powershell"}
    context_definition, context_call = context_helpers(lab, "", force_azure=cloud_cleanup)
    if lab["track"] == "azure-cli":
        adapter = r"""
function Invoke-AzCliCleanupCommand {
    [CmdletBinding()]
    param([Parameter(Mandatory)][string[]]$ArgumentList)
    $savedNativePreference = $PSNativeCommandUseErrorActionPreference
    try {
        $PSNativeCommandUseErrorActionPreference = $false
        $outputLines = @(& az @ArgumentList)
        $nativeExit = $LASTEXITCODE
    }
    finally {
        $PSNativeCommandUseErrorActionPreference = $savedNativePreference
    }
    return [pscustomobject]@{ ExitCode = $nativeExit; Output = @($outputLines) }
}
"""
        operation = f"""        $showResult = Invoke-AzCliCleanupCommand -ArgumentList @('resource', 'show', '--ids', $managed.id, '--output', 'json', '--only-show-errors')
        if ($showResult.ExitCode -eq 3) {{
            Complete-ManagedObject -ManagedId $managed.id -Result absent
            continue
        }}
        if ($showResult.ExitCode -ne 0) {{ throw "Azure CLI ownership inspection exited with code $($showResult.ExitCode)." }}
        $rawResource = @($showResult.Output) -join "`n"
        if ([string]::IsNullOrWhiteSpace($rawResource)) {{ throw 'Azure CLI ownership inspection returned no resource.' }}
        try {{ $liveResource = $rawResource | ConvertFrom-Json -Depth 100 }} catch {{ throw 'Azure CLI ownership inspection returned invalid JSON.' }}
        if ([string]$liveResource.id -ine [string]$managed.id) {{ throw 'Live resource ID does not exactly match run state.' }}
        Assert-ExactLiveOwnership -Tags $liveResource.tags -Managed $managed
        $deleteResult = Invoke-AzCliCleanupCommand -ArgumentList @('resource', 'delete', '--ids', $managed.id, '--only-show-errors')
        if ($deleteResult.ExitCode -ne 0) {{ throw "Azure CLI deletion exited with code $($deleteResult.ExitCode)." }}
        Complete-ManagedObject -ManagedId $managed.id -Result removed"""
    elif lab["track"] == "azure-powershell":
        adapter = ""
        operation = f"""        $liveResource = $null
        try {{ $liveResource = Get-AzResource -ResourceId $managed.id -ErrorAction Stop }}
        catch {{
            $lookupError = "$($_.FullyQualifiedErrorId) $($_.Exception.Message)"
            if ($lookupError -match '(?i)\\b(?:ResourceNotFound|ResourceGroupNotFound|could not be found|was not found)\\b') {{
                Complete-ManagedObject -ManagedId $managed.id -Result absent
                continue
            }}
            throw
        }}
        if ($null -eq $liveResource) {{
            Complete-ManagedObject -ManagedId $managed.id -Result absent
            continue
        }}
        if ([string]$liveResource.ResourceId -ine [string]$managed.id) {{ throw 'Live resource ID does not exactly match run state.' }}
        Assert-ExactLiveOwnership -Tags $liveResource.Tags -Managed $managed
        Remove-AzResource -ResourceId $managed.id -Force -ErrorAction Stop | Out-Null
        Complete-ManagedObject -ManagedId $managed.id -Result removed"""
    else:
        adapter = ""
        operation = "        throw 'An offline design-simulation run cannot own a cloud resource.'"
    return common_parameters(lab, content) + f"""
$LabRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$StateRoot = Join-Path $LabRoot ".state/$RunId"
$RunPath = Join-Path $StateRoot 'run.json'
$CleanupPath = Join-Path $StateRoot 'cleanup.json'
{context_definition}
{adapter}

function Save-RunState {{
    [CmdletBinding()]
    param([Parameter(Mandatory)]$State)
    $temporaryPath = "$RunPath.tmp"
    $State | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $temporaryPath -Encoding utf8NoBOM
    Move-Item -LiteralPath $temporaryPath -Destination $RunPath -Force
}}

function Save-CleanupArtifact {{
    [CmdletBinding()]
    param(
        [ValidateSet('pass', 'partial', 'fail')][string]$Result,
        [bool]$OwnershipVerified
    )
    $artifact = [ordered]@{{
        schemaVersion = '1.0.0'; labId = '{lab['id']}'; runId = $RunId; result = $Result
        completedAt = (Get-Date).ToUniversalTime().ToString('o'); ownershipVerified = $OwnershipVerified
        activeManagedObjects = @($state.managedObjects).Count; actions = @($actions)
    }}
    $temporaryPath = "$CleanupPath.tmp"
    $artifact | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $temporaryPath -Encoding utf8NoBOM
    Move-Item -LiteralPath $temporaryPath -Destination $CleanupPath -Force
}}

function Assert-ExactLiveOwnership {{
    [CmdletBinding()]
    param($Tags, $Managed)
    if ($null -eq $Tags) {{ throw 'Live resource has no ownership tags.' }}
    $valid = (
        [string]$Tags.purpose -ceq 'az305-lab' -and
        [string]$Tags.labId -ceq '{lab['id']}' -and
        [string]$Tags.runId -ceq $RunId -and
        [string]$Tags.expiresOn -ceq [string]$Managed.tags.expiresOn
    )
    if (-not $valid) {{ throw 'Live ownership tags do not exactly match run state.' }}
}}

function Complete-ManagedObject {{
    [CmdletBinding()]
    param([Parameter(Mandatory)][string]$ManagedId, [ValidateSet('removed', 'absent')][string]$Result)
    $state.managedObjects = @($state.managedObjects | Where-Object {{ [string]$_.id -ine $ManagedId }})
    # Settings for a deleted run-owned object or its descendants no longer need restoration.
    $state.originalSettings = @($state.originalSettings | Where-Object {{
        $settingId = [string]$_.id
        -not ($settingId -ieq $ManagedId -or $settingId.StartsWith("$ManagedId/", [System.StringComparison]::OrdinalIgnoreCase))
    }})
    Save-RunState -State $state
    $actions.Add([pscustomobject]@{{ id = $ManagedId; result = $Result }})
}}

if (-not (Test-Path -LiteralPath $RunPath)) {{ Write-Warning 'No run state exists; cleanup is gated.'; exit 2 }}
try {{ $state = Get-Content -LiteralPath $RunPath -Raw | ConvertFrom-Json -Depth 100 }}
catch {{ [Console]::Error.WriteLine('Cleanup refused because run state is not valid JSON.'); exit 1 }}
$actions = [System.Collections.Generic.List[object]]::new()
$identityValid = (
    $state.labId -ceq '{lab['id']}' -and
    $state.runId -ceq $RunId -and
    $state.track -ceq '{lab['track']}' -and
    $state.implementationMode -ceq '{lab['implementationMode']}'
)
if (-not $identityValid) {{
    $actions.Add([pscustomobject]@{{ id = 'identity-check'; result = 'refused' }})
    Save-CleanupArtifact -Result fail -OwnershipVerified $false
    [Console]::Error.WriteLine('Cleanup refused because the lab, run, track, mode, tenant, or subscription does not exactly match run state.')
    exit 1
}}

if (@($state.managedObjects).Count -gt 0 -and (
    [string]::IsNullOrWhiteSpace($SubscriptionId) -or
    [string]::IsNullOrWhiteSpace($TenantId) -or
    [string]$state.parameters.subscriptionId -ine $SubscriptionId -or
    [string]$state.parameters.tenantId -ine $TenantId
)) {{
    $actions.Add([pscustomobject]@{{ id = 'context-record'; result = 'refused' }})
    Save-CleanupArtifact -Result fail -OwnershipVerified $false
    [Console]::Error.WriteLine('Cleanup refused because the requested tenant and subscription do not exactly match run state.')
    exit 1
}}

$ownershipValid = $true
foreach ($managed in @($state.managedObjects)) {{
    $valid = (
        $managed.id -and
        [string]$managed.id -match '^/subscriptions/([^/]+)/' -and
        $Matches[1] -ieq $SubscriptionId -and
        [string]$managed.tags.purpose -ceq 'az305-lab' -and
        [string]$managed.tags.labId -ceq '{lab['id']}' -and
        [string]$managed.tags.runId -ceq $RunId -and
        -not [string]::IsNullOrWhiteSpace([string]$managed.tags.expiresOn) -and
        [string]$managed.tags.expiresOn -ceq [string]$state.parameters.expiresOn
    )
    if (-not $valid) {{ $ownershipValid = $false }}
}}
if (-not $ownershipValid) {{
    $actions.Add([pscustomobject]@{{ id = 'ownership-check'; result = 'refused' }})
    Save-CleanupArtifact -Result fail -OwnershipVerified $false
    [Console]::Error.WriteLine('Cleanup refused because recorded IDs and ownership tags could not be proven exactly.')
    exit 1
}}

if (@($state.managedObjects).Count -eq 0 -and @($state.originalSettings).Count -gt 0) {{
    $state.status = 'failed'
    Save-RunState -State $state
    $actions.Add([pscustomobject]@{{ id = 'original-settings'; result = 'refused' }})
    Save-CleanupArtifact -Result fail -OwnershipVerified $false
    [Console]::Error.WriteLine('Cleanup refused because original settings remain without a run-owned object whose deletion can safely restore the boundary.')
    exit 1
}}

{("if ($Execute -and @($state.managedObjects).Count -gt 0) { $actions.Add([pscustomobject]@{ id = 'implementation-mode'; result = 'refused' }); Save-CleanupArtifact -Result fail -OwnershipVerified $false; [Console]::Error.WriteLine('Design-simulation cleanup refuses cloud objects and will not issue a query or delete.'); exit 1 }" if lab["implementationMode"] == "design-simulation" else "# This implementation mode may clean only exact run-owned cloud objects.")}

$orderedObjects = @($state.managedObjects)
[array]::Reverse($orderedObjects)
if (@($state.managedObjects).Count -eq 0) {{
    $state.status = 'cleaned'
    Save-RunState -State $state
    Save-CleanupArtifact -Result pass -OwnershipVerified $true
    exit 0
}}

if (-not $Execute) {{
    foreach ($managed in $orderedObjects) {{ $actions.Add([pscustomobject]@{{ id = $managed.id; result = 'planned' }}) }}
    Save-CleanupArtifact -Result partial -OwnershipVerified $true
    Write-Output '[preview] Dependency-aware cleanup plan written; no cloud command was called.'
    exit 2
}}

try {{
    {context_call}
}}
catch {{
    $actions.Add([pscustomobject]@{{ id = 'context-check'; result = 'refused' }})
    Save-CleanupArtifact -Result partial -OwnershipVerified $false
    [Console]::Error.WriteLine("Cleanup is gated by exact context validation: $($_.Exception.Message)")
    exit 2
}}

# Persist the cleanup transition before the first possible delete.
$state.status = 'cleaning'
Save-RunState -State $state
$cleanupFailed = $false
foreach ($managed in $orderedObjects) {{
    try {{
        # State is necessary but not sufficient: inspect the exact live ID and tags immediately before removal.
{operation}
    }} catch {{
        $actions.Add([pscustomobject]@{{ id = $managed.id; result = 'failed' }})
        $cleanupFailed = $true
        break
    }}
}}
if ($cleanupFailed -or @($state.managedObjects).Count -gt 0 -or @($state.originalSettings).Count -gt 0) {{
    $state.status = 'failed'
    Save-RunState -State $state
    Save-CleanupArtifact -Result partial -OwnershipVerified $false
    exit 1
}}
$state.status = 'cleaned'
Save-RunState -State $state
Save-CleanupArtifact -Result pass -OwnershipVerified $true
exit 0
"""


def architecture_mermaid(lab: dict[str, Any], content: dict[str, Any]) -> str:
    def clean(value: str) -> str:
        return value.replace('"', "'").replace("[", "(").replace("]", ")")
    lines = ["flowchart LR", f"    R[\"{clean(content['businessOutcome'])}\"]"]
    previous = "R"
    for index, cp in enumerate(content["checkpoints"], 1):
        node = f"C{index}"
        lines.append(f"    {previous} --> {node}[\"{clean(cp['title'])}\"]")
        previous = node
    lines.append(f"    {previous} --> E[\"Independent positive and negative evidence\"]")
    lines.append("    classDef boundary fill:#eef5ff,stroke:#005a9e,color:#111")
    lines.append("    class R,E boundary")
    return "\n".join(lines) + "\n"


def matrix_markdown(decision: dict[str, Any]) -> str:
    headers = "| Candidate | Eligible | C1 | C2 | C3 | C4 | C5 | Weighted /100 |\n| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"
    rows = []
    for item in decision["candidates"]:
        scores = item["scores"]
        rows.append(f"| {markdown_escape(item['name'])} | {'yes' if item['eligible'] else 'no'} | {scores['C1']} | {scores['C2']} | {scores['C3']} | {scores['C4']} | {scores['C5']} | {item['weightedTotal']:.0f} |")
    return headers + "\n" + "\n".join(rows)


def navigation(lab: dict[str, Any], catalog: dict[str, Any]) -> str:
    by_id = {item["id"]: item for item in catalog["labs"]}
    links = []
    if lab["previousLabId"]:
        prev = by_id[lab["previousLabId"]]
        links.append(f"[← {prev['id']}](../{prev['folder']}/README.md)")
    links.append("[Lab catalog](../README.md)")
    if lab["nextLabId"]:
        nxt = by_id[lab["nextLabId"]]
        links.append(f"[{nxt['id']} →](../{nxt['folder']}/README.md)")
    return " · ".join(links)


def readme(lab: dict[str, Any], content: dict[str, Any], objectives: list[str], requirements: dict[str, Any], decision: dict[str, Any], scripts: dict[str, str], catalog: dict[str, Any]) -> str:
    number = lab["number"]
    objective_rows = []
    for index, cp in enumerate(content["checkpoints"], 1):
        for objective in checkpoint_objectives(objectives, index):
            objective_rows.append(f"| `{objective}` | `{cp['requirement']}` | [`LAB{number}-CP0{index}`](#checkpoint-{index}) |")
    checkpoint_text = []
    for index, cp in enumerate(content["checkpoints"], 1):
        objective = "`, `".join(checkpoint_objectives(objectives, index))
        checkpoint_text.append(f"""### Checkpoint {index}: {cp['title']}

<a id="checkpoint-{index}"></a>

**Trace:** `{objective}` → `{cp['requirement']}` → `LAB{number}-CP0{index}`

```powershell
{cp['command']}
```

Expected evidence: {cp['expected']} Retain {cp['evidence']}

Positive assertion:

```powershell
{cp.get('positiveCommand', "Write-Output 'Positive assertion is described in the validation contract.'")}
```

Negative assertion:

```powershell
{cp.get('negativeCommand', "Write-Output 'Negative assertion is described in the validation contract.'")}
```

Failure and retry: {cp['failure']} {cp['retry']}

Cleanup dependency: {cp['cleanup']}

WAF consequence: {cp['waf']}
""")
    req_list = "\n".join(f"- `{item['id']}` — {item['statement']}" for item in requirements["functionalRequirements"] + requirements["nonfunctionalRequirements"])
    fact_labels = {
        "data": "Data", "scale": "Scale", "latency": "Latency", "availability": "Availability",
        "rto": "RTO", "rpo": "RPO", "budget": "Budget",
    }
    facts = "\n".join(f"- **{fact_labels[key]}:** {requirements['facts'][key]}" for key in fact_labels)
    constraints = "\n".join(f"- {item}" for item in requirements["constraints"])
    assumptions = "\n".join(f"- {item}" for item in requirements["assumptions"])
    candidate_lines = []
    for candidate in decision["candidates"]:
        status = "eligible" if candidate["eligible"] else "ineligible"
        line = f"- **{candidate['name']}** ({status}) — {candidate['rationale']}"
        if candidate["disqualifiers"]:
            line += " Disqualifier: " + " ".join(candidate["disqualifiers"])
        candidate_lines.append(line)
    candidates = "\n".join(candidate_lines)
    rejections = "\n".join(f"- **{item['candidate']}:** {item['reason']}" for item in decision["rejectedAlternatives"])
    risks = "\n".join(f"- **Risk:** {item['risk']} **Mitigation:** {item['mitigation']}" for item in decision["risks"])
    waf = "\n".join(
        f"- **{label}:** {decision['waf'][key]}"
        for key, label in (
            ("reliability", "Reliability"), ("security", "Security"),
            ("costOptimization", "Cost Optimization"), ("operationalExcellence", "Operational Excellence"),
            ("performanceEfficiency", "Performance Efficiency"),
        )
    )
    revised_waf = "\n".join(
        f"- **{label}:** {decision['revisedDecision']['waf'][key]}"
        for key, label in (
            ("reliability", "Reliability"), ("security", "Security"),
            ("costOptimization", "Cost Optimization"), ("operationalExcellence", "Operational Excellence"),
            ("performanceEfficiency", "Performance Efficiency"),
        )
    )
    adr_consequences = "\n".join(f"- {item}" for item in decision["adr"]["consequences"])
    safe = decision["safeAnalogue"] or "The reference topology is deployable at bounded scope; preview remains the default and live verification is separate."
    appendix = []
    for name in ("Preflight.ps1", "Setup.ps1", "Validate.ps1", "Cleanup.ps1"):
        appendix.append(f"### {name}\n\n```powershell\n{scripts[name].rstrip()}\n```")
    sources = f"- [{content['primarySource']['title']}]({content['primarySource']['url']})\n- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/)"
    return f"""# {lab['id']} — {lab['title']}

## 1. Navigation

{navigation(lab, catalog)}

## 2. Scenario and completion contract

{content['scenario']}

- Architect role: {content['role']}
- Outcome: {content['outcome']}
- Duration: {content['duration']}
- Difficulty: {content['difficulty']}
- Cost class: {content['costClass']}
- Completion: all five checkpoint assertions, final validation, decision revision, and cleanup review are complete.

## 3. Objective-to-evidence map

| Objective | Requirement | Checkpoint |
| --- | --- | --- |
{chr(10).join(objective_rows)}

## 4. Business and quality requirements

Business outcome: {content['businessOutcome']}

{req_list}

Scenario facts:

{facts}

Constraints:

{constraints}

Assumptions:

{assumptions}

## 5. Architecture diagram and walkthrough

![Accessible architecture for {lab['title']}](diagrams/architecture.svg)

The flow begins with the business outcome, crosses five independently validated design capabilities, and ends with positive and negative evidence. The SVG is deterministically rendered from `diagrams/architecture.mmd`.

## 6. Concept primer and candidate architectures

Architecture decisions translate measurable requirements into a deliberate service and operating model. A candidate is viable only when every mandatory constraint is met; convenience or familiarity cannot compensate for a disqualifier.

{candidates}

## 7. Decision, ADR, and Well-Architected review

Criteria weights are C1 30, C2 25, C3 20, C4 15, and C5 10. Weighted totals use `sum(weight × score) / 5`.

{matrix_markdown(decision)}

Selected design: **{decision['selectedCandidate']}**. `{decision['adr']['id']}` records the accepted reasoning. Review Reliability, Security, Cost Optimization, Operational Excellence, and Performance Efficiency in `design/decision.yml`; no pillar is implied by another.

Rejected alternatives:

{rejections}

Architecture risks:

{risks}

Well-Architected consequences:

{waf}

ADR consequences:

{adr_consequences}

## 8. Inputs, permissions, licensing, cost, and analogue

Use configurable `Location` (`AZ305_LOCATION`, default West Europe) and `SecondaryLocation` (`AZ305_SECONDARY_LOCATION`, default North Europe). Every public input has an explicit `AZ305_*` fallback. Preview is the default; only Golden Lab 00 writes an intent-only `execute: false` preview record. Before an executed cloud command, the supplied subscription and tenant must exactly match the active CLI, Az, and—where applicable—Microsoft Graph contexts. `-Execute` crosses the execution boundary; cost-bearing and tenant-scoped paths also require their independent acknowledgement switches.

Safe analogue: {safe}

Permissions: {content['architectureAnalysis']['permissions']}

Licensing: {content['architectureAnalysis']['licensing']}

Cost boundary: {content['architectureAnalysis']['costNotes']}

## 9. Read-only preflight

```powershell
pwsh ./scripts/{lab['track']}/Preflight.ps1 -RunId synthetic-{number}0001
```

Synthetic sample: `{{"labId":"{lab['id']}","track":"{lab['track']}","result":"pass","note":"Local tool discovery only"}}`. This is illustrative local output, not evidence captured from Azure.

## 10. Five guided checkpoints

{(chr(10) * 2).join(item.rstrip() for item in checkpoint_text)}

## 11. Final validation and interpretation

Run `Validate.ps1 -Mode Deployment -Execute` only after an executed run has state and you are authorized to issue the ten read-only checkpoint inspections. Without `-Execute`, ordinary deployment validation records `partial` and exits `2`; Golden Lab 00 alone can validate its intent-only preview locally. Exit `0` means all required assertions pass, `1` means at least one failed, and `2` means the outcome is gated or partial. Positive and negative commands execute independently, so one failure never suppresses its paired assertion.

## 12. Material change request

{content['changeRequest']}

Revised solution: select **{decision['revisedDecision']['selectedCandidate']}**. {decision['revisedDecision']['reason']}

Revised Well-Architected consequences:

{revised_waf}

## 13. Architect job challenge

{content['challenge']}

## 14. Troubleshooting, cleanup, and residual verification

{chr(10).join('- ' + item for item in content['troubleshooting'])}

Cleanup previews nonempty state in reverse dependency order, writes `partial`, and exits `2`; an already empty run is completed locally and idempotently. Executed cleanup rechecks the exact live ID plus `purpose`, `labId`, `runId`, and `expiresOn` immediately before each removal, persists state after every absent or removed object, stops on the first dependency failure, and refuses unresolved pre-existing settings. It never automates purge. Finish with `Validate.ps1 -Mode PostCleanup`; the required residual count is zero.

## 15. Exam debrief, assessment, sources, and navigation

Explain the recommendation in terms of requirements, rejected alternatives, failure behavior, and all five WAF pillars. {('Complete `assessment/QUESTIONS.md`, then use the separately excluded answer key for remediation.' if 1 <= int(number) <= 25 else 'This foundation or capstone reinforces the curriculum and has no scored question bank.')}

{sources}

{navigation(lab, catalog)}

## 16. Synchronized lifecycle-script appendix

{(chr(10) * 2).join(appendix)}
"""


def solution_readme(lab: dict[str, Any], content: dict[str, Any], decision: dict[str, Any]) -> str:
    selected = next(item for item in decision["candidates"] if item["name"] == decision["selectedCandidate"])
    rejected = "\n".join(f"- **{item['candidate']}:** {item['reason']}" for item in decision["rejectedAlternatives"])
    risks = "\n".join(f"- **{item['risk']}** — {item['mitigation']}" for item in decision["risks"])
    current_waf = "\n".join(f"- **{key}:** {value}" for key, value in decision["waf"].items())
    revised_waf = "\n".join(f"- **{key}:** {value}" for key, value in decision["revisedDecision"]["waf"].items())
    return f"""# {lab['id']} solution rationale

The recommended architecture is **{decision['selectedCandidate']}** with a weighted total of {selected['weightedTotal']:.0f}/100. {selected['rationale']} The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

{rejected}

## Risks and mitigations

{risks}

## Initial Well-Architected consequences

{current_waf}

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: {content['changeRequest']}

The revised decision is **{decision['revisedDecision']['selectedCandidate']}**. {decision['revisedDecision']['reason']} Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

{revised_waf}

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
"""


def tests_readme(lab: dict[str, Any]) -> str:
    return f"""# {lab['id']} offline tests

Run `Invoke-Pester ./tests/Contract.Tests.ps1 -CI` from this copied lab folder. The suite installs throwing in-session shims for Azure CLI, Az, Microsoft Graph, REST, AzCopy, and migration entry points. It proves preview safety, state ordering, recoverability, independent assertions, exact ownership refusal, reverse dependency cleanup, idempotence, and a zero-residual post-cleanup fixture.
"""


def pester_test_value(name: str) -> str:
    if name in INTEGER_INPUTS:
        return "1"
    if name in BOOLEAN_INPUTS:
        return "$false"
    if re.search(r"(?:ResourceId|DcrId|VmId|SubnetId|WorkspaceId)$", name):
        return ps_single("/subscriptions/00000000-0000-4000-8000-000000000305/resourceGroups/rg-az305-contract/providers/Microsoft.Test/resources/synthetic")
    if name.endswith(("ObjectId", "PrincipalId")):
        return ps_single("00000000-0000-4000-8000-000000000307")
    if name.endswith("Json"):
        return ps_single("{}")
    if "Fqdn" in name or "Endpoint" in name:
        return ps_single("service.example.invalid")
    if name.endswith("Ip") or "IPAddress" in name:
        return ps_single("192.0.2.10")
    return ps_single(f"synthetic-{re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()}")


def pester_tests(lab: dict[str, Any], content: dict[str, Any]) -> str:
    track = lab["track"]
    corpus = "\n".join(
        str(cp.get(field, ""))
        for cp in content["checkpoints"]
        for field in ("command", "positiveCommand", "negativeCommand")
    )
    setup_corpus = "\n".join(str(cp["command"]) for cp in content["checkpoints"])
    validation_corpus = "\n".join(
        str(cp.get(field, "")) for cp in content["checkpoints"] for field in ("positiveCommand", "negativeCommand")
    )
    cmdlets = sorted(set(re.findall(
        r"\b(?:Get|New|Set|Remove|Update|Test|Invoke|Start|Stop|Enable|Disable)-(?:Az|Mg)[A-Za-z0-9.]*\b",
        corpus,
        re.IGNORECASE,
    )))
    cmdlets = [name for name in cmdlets if name.casefold() not in {"get-azcontext", "get-mgcontext"}]
    cloud_failure_functions = "\n".join(
        f"function global:{name} {{ Record-Az305TestCall -Name {ps_single(name)}; throw 'Injected checkpoint failure.' }}"
        for name in cmdlets
    )
    input_lines = "\n".join(f"        {name} = {pester_test_value(name)}" for name in discover_inputs(content))
    design = "$true" if lab["implementationMode"] == "design-simulation" else "$false"
    setup_design_cloud = "$true" if lab["implementationMode"] == "design-simulation" and command_uses_cloud(setup_corpus, track) else "$false"
    validation_design_cloud = "$true" if lab["implementationMode"] == "design-simulation" and command_uses_cloud(validation_corpus, track) else "$false"
    is_cli = "$true" if track == "azure-cli" else "$false"
    partial_deployment_test = ""
    if deployment_create_indexes := {
        index for index, checkpoint in enumerate(content["checkpoints"], 1)
        if is_deployment_create(str(checkpoint["command"]))
    }:
        partial_deployment_test = f"""
    It 'retains exact planned child IDs after a native deployment failure and can clean them' {{
        $run = 'partial-deploy-000001'
        $parentId = "/subscriptions/$SubscriptionId/resourceGroups/rg-az305-contract/providers/Microsoft.Test/parents/one"
        $childId = "$parentId/children/two"
        $partialShim = $ShimPreamble + @'
function global:az {{
    if ($args[0] -eq 'account' -and $args[1] -eq 'show') {{ $global:LASTEXITCODE = 0; return '{{"id":"00000000-0000-4000-8000-000000000305","tenantId":"00000000-0000-4000-8000-000000000306"}}' }}
    if ($args[0] -eq 'vm' -or $args[0] -eq 'bicep') {{ $global:LASTEXITCODE = 0; return '{{}}' }}
    if ($args[0] -eq 'deployment' -and $args[2] -eq 'what-if') {{
        $global:LASTEXITCODE = 0
        return '{{"changes":[{{"resourceId":"__PARENT__","changeType":"Create"}},{{"resourceId":"__CHILD__","changeType":"Create"}}]}}'
    }}
    if ($args[0] -eq 'deployment' -and $args[2] -eq 'create') {{ Record-Az305TestCall -Name 'partial-deployment'; $global:LASTEXITCODE = 17; return }}
    throw 'Unexpected command in partial-deployment simulation.'
}}
'@.Replace('__PARENT__', $parentId).Replace('__CHILD__', $childId)
        $setup = Invoke-LifecycleProcess -ScriptName 'Setup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $partialShim
        $setup.ExitCode | Should -Be 1
        $statePath = Join-Path $IsolatedLab ".state/$run/run.json"
        $state = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
        $state.status | Should -Be 'failed'
        @($state.managedObjects).Count | Should -Be 2
        @($state.managedObjects.id) | Should -Contain $parentId
        @($state.managedObjects.id) | Should -Contain $childId
        (Get-Content -LiteralPath $CallLog | Select-Object -First 1) | Should -Match 'partial-deployment\\|state=True'
        $cleanup = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody (Get-CleanupSuccessShim)
        $cleanup.ExitCode | Should -Be 0
        $deleteOrder = @(Get-Content -LiteralPath $CallLog | Where-Object {{ $_ -match '^/subscriptions/' }})
        $deleteOrder | Should -Be @($childId, $parentId)
        $finalState = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
        @($finalState.managedObjects).Count | Should -Be 0
    }}
"""
    return f"""[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Pester lifecycle variables cross BeforeAll, BeforeEach, helper, and It scopes.')]
param()

BeforeAll {{
    $SourceLabRoot = Split-Path $PSScriptRoot -Parent
    $Track = '{track}'
    $IsDesignSimulation = {design}
    $IsFoundationPreview = {('$true' if lab['id'] == 'LAB-00' else '$false')}
    $SetupHasDesignCloudGate = {setup_design_cloud}
    $ValidationHasDesignCloudGate = {validation_design_cloud}
    $IsCliTrack = {is_cli}
    $SubscriptionId = '00000000-0000-4000-8000-000000000305'
    $TenantId = '00000000-0000-4000-8000-000000000306'
    $BaseParameters = [ordered]@{{
        SubscriptionId = $SubscriptionId
        TenantId = $TenantId
        Location = 'westeurope'
        SecondaryLocation = 'northeurope'
        ResourceGroup = 'rg-az305-contract'
        WorkloadName = 'az305-contract'
        ExpiresOn = '2099-12-31'
{input_lines}
    }}

    $ShimPreamble = @'
function global:Record-Az305TestCall {{
    param([string]$Name)
    if ($env:AZ305_TEST_CALL_LOG) {{
        $stateExists = Test-Path -LiteralPath $env:AZ305_TEST_STATE_PATH
        Add-Content -LiteralPath $env:AZ305_TEST_CALL_LOG -Value "$Name|state=$stateExists"
    }}
}}
function global:Invoke-AzRestMethod {{ Record-Az305TestCall -Name 'Invoke-AzRestMethod'; throw 'Unexpected Azure REST request.' }}
function global:Connect-MgGraph {{ Record-Az305TestCall -Name 'Connect-MgGraph'; throw 'Lifecycle scripts must never sign in.' }}
function global:Invoke-MgGraphRequest {{ Record-Az305TestCall -Name 'Invoke-MgGraphRequest'; throw 'Unexpected Microsoft Graph request.' }}
function global:Start-AzDataMigration {{ Record-Az305TestCall -Name 'Start-AzDataMigration'; throw 'Unexpected migration request.' }}
'@
    $MatchingFailureShim = $ShimPreamble + @'
function global:az {{
    if ($args.Count -ge 2 -and $args[0] -eq 'account' -and $args[1] -eq 'show') {{
        $global:LASTEXITCODE = 0
        return '{{"id":"00000000-0000-4000-8000-000000000305","tenantId":"00000000-0000-4000-8000-000000000306"}}'
    }}
    Record-Az305TestCall -Name ('az ' + ($args -join ' '))
    $global:LASTEXITCODE = 17
    return '{{}}'
}}
function global:Get-AzContext {{
    return [pscustomobject]@{{ Subscription = [pscustomobject]@{{ Id = '00000000-0000-4000-8000-000000000305' }}; Tenant = [pscustomobject]@{{ Id = '00000000-0000-4000-8000-000000000306' }} }}
}}
function global:Get-MgContext {{ return [pscustomobject]@{{ TenantId = '00000000-0000-4000-8000-000000000306' }} }}
{cloud_failure_functions}
function global:azcopy {{ Record-Az305TestCall -Name 'azcopy'; $global:LASTEXITCODE = 17; return '{{}}' }}
function global:bicep {{ Record-Az305TestCall -Name 'bicep'; $global:LASTEXITCODE = 17; return '{{}}' }}
'@
    $ContextMismatchShim = $ShimPreamble + @'
function global:az {{
    if ($args.Count -ge 2 -and $args[0] -eq 'account' -and $args[1] -eq 'show') {{
        $global:LASTEXITCODE = 0
        return '{{"id":"00000000-0000-4000-8000-000000009999","tenantId":"00000000-0000-4000-8000-000000009998"}}'
    }}
    Record-Az305TestCall -Name 'unexpected-az'
    throw 'A checkpoint command ran after context mismatch.'
}}
function global:Get-AzContext {{ return [pscustomobject]@{{ Subscription = [pscustomobject]@{{ Id = '00000000-0000-4000-8000-000000009999' }}; Tenant = [pscustomobject]@{{ Id = '00000000-0000-4000-8000-000000009998' }} }} }}
function global:Get-MgContext {{ return [pscustomobject]@{{ TenantId = '00000000-0000-4000-8000-000000009998' }} }}
'@
    $OfflineRefusalShim = $ShimPreamble + @'
function global:az {{ Record-Az305TestCall -Name 'forbidden-az'; throw 'Design simulation issued an Azure CLI request.' }}
function global:Get-AzContext {{ Record-Az305TestCall -Name 'forbidden-Get-AzContext'; throw 'Design simulation issued an Az request.' }}
function global:Get-MgContext {{ Record-Az305TestCall -Name 'forbidden-Get-MgContext'; throw 'Design simulation issued a Graph request.' }}
{cloud_failure_functions}
function global:azcopy {{ Record-Az305TestCall -Name 'forbidden-azcopy'; throw 'Design simulation issued an AzCopy request.' }}
'@
}}

Describe '{lab['id']} portable lifecycle behavior' {{
    BeforeEach {{
        $IsolatedLab = Join-Path $TestDrive ("lab-" + [guid]::NewGuid().ToString('N'))
        Copy-Item -LiteralPath $SourceLabRoot -Destination $IsolatedLab -Recurse
        $ScriptRoot = Join-Path $IsolatedLab "scripts/$Track"
        $CallLog = Join-Path $IsolatedLab 'cloud-calls.log'
        $env:AZ305_TEST_CALL_LOG = $CallLog
    }}

    AfterEach {{
        Remove-Item Env:AZ305_TEST_CALL_LOG -ErrorAction SilentlyContinue
        Remove-Item Env:AZ305_TEST_STATE_PATH -ErrorAction SilentlyContinue
        Remove-Item Env:AZ305_TEST_RUN_ID -ErrorAction SilentlyContinue
    }}

    BeforeAll {{
    function Get-TestParameterSet {{
        param([string]$RunId, [switch]$Execute, [string]$Mode)
        $parameters = @{{}}
        foreach ($entry in $BaseParameters.GetEnumerator()) {{ $parameters[$entry.Key] = $entry.Value }}
        $parameters.RunId = $RunId
        if ($Execute) {{
            $parameters.Execute = $true
            $parameters.AcknowledgeCost = $true
            $parameters.AcknowledgeTenantChange = $true
        }}
        if ($Mode) {{ $parameters.Mode = $Mode }}
        return $parameters
    }}

    function Invoke-LifecycleProcess {{
        param([string]$ScriptName, [hashtable]$Parameters, [string]$ShimBody = '')
        $invocationId = [guid]::NewGuid().ToString('N')
        $parametersPath = Join-Path $IsolatedLab "$invocationId.parameters.json"
        $harnessPath = Join-Path $IsolatedLab "$invocationId.harness.ps1"
        $Parameters | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $parametersPath -Encoding utf8NoBOM
        $harness = @'
param([string]$TargetScript, [string]$ParametersPath)
'@ + "`n" + $ShimBody + @'
$invokeParameters = Get-Content -LiteralPath $ParametersPath -Raw | ConvertFrom-Json -AsHashtable
& $TargetScript @invokeParameters
exit $LASTEXITCODE
'@
        $harness | Set-Content -LiteralPath $harnessPath -Encoding utf8NoBOM
        $env:AZ305_TEST_RUN_ID = [string]$Parameters.RunId
        $env:AZ305_TEST_STATE_PATH = Join-Path $IsolatedLab ".state/$($Parameters.RunId)/run.json"
        $savedNativePreference = $PSNativeCommandUseErrorActionPreference
        try {{
            $PSNativeCommandUseErrorActionPreference = $false
            $output = @(& pwsh -NoLogo -NoProfile -File $harnessPath -TargetScript (Join-Path $ScriptRoot $ScriptName) -ParametersPath $parametersPath 2>&1)
            $exitCode = $LASTEXITCODE
        }}
        finally {{ $PSNativeCommandUseErrorActionPreference = $savedNativePreference }}
        return [pscustomobject]@{{ ExitCode = $exitCode; Output = @($output) }}
    }}

    function Write-TestRunState {{
        param([string]$RunId, [string]$Status = '{"planned" if lab["implementationMode"] == "design-simulation" or lab["id"] in {"LAB-21", "LAB-26"} else "deployed"}', [object[]]$ManagedObjects = @(), [object[]]$OriginalSettings = @())
        $stateRoot = Join-Path $IsolatedLab ".state/$RunId"
        New-Item -ItemType Directory -Path $stateRoot -Force | Out-Null
        $state = [ordered]@{{
            schemaVersion = '1.0.0'; labId = '{lab['id']}'; runId = $RunId; track = '{track}'
            implementationMode = '{lab['implementationMode']}'; status = $Status
            createdAt = '2026-09-02T00:00:00Z'; execute = $true
            parameters = [ordered]@{{ subscriptionId = $SubscriptionId; tenantId = $TenantId; expiresOn = '2099-12-31' }}
            managedObjects = @($ManagedObjects); originalSettings = @($OriginalSettings)
        }}
        $path = Join-Path $stateRoot 'run.json'
        $state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $path -Encoding utf8NoBOM
        return $path
    }}

    function Get-ManagedObjectFixture {{
        param([string]$Id, [string]$RunId, [string]$RecordedRunId = $RunId)
        return [pscustomobject]@{{
            id = $Id; type = 'azure-resource'
            tags = [ordered]@{{ purpose = 'az305-lab'; labId = '{lab['id']}'; runId = $RecordedRunId; expiresOn = '2099-12-31' }}
        }}
    }}

    function Get-CleanupSuccessShim {{
        if ($IsCliTrack) {{
            return $ShimPreamble + @'
function global:az {{
    if ($args[0] -eq 'account' -and $args[1] -eq 'show') {{ $global:LASTEXITCODE = 0; return '{{"id":"00000000-0000-4000-8000-000000000305","tenantId":"00000000-0000-4000-8000-000000000306"}}' }}
    $idIndex = [Array]::IndexOf([object[]]$args, '--ids')
    $id = [string]$args[$idIndex + 1]
    if ($args[0] -eq 'resource' -and $args[1] -eq 'show') {{
        $global:LASTEXITCODE = 0
        return ([ordered]@{{ id = $id; tags = [ordered]@{{ purpose = 'az305-lab'; labId = '__LAB_ID__'; runId = $env:AZ305_TEST_RUN_ID; expiresOn = '2099-12-31' }} }} | ConvertTo-Json -Compress)
    }}
    if ($args[0] -eq 'resource' -and $args[1] -eq 'delete') {{ Add-Content -LiteralPath $env:AZ305_TEST_CALL_LOG -Value $id; $global:LASTEXITCODE = 0; return }}
    throw 'Unexpected Azure CLI cleanup command.'
}}
'@.Replace('__LAB_ID__', '{lab['id']}')
        }}
        return $ShimPreamble + @'
function global:Get-AzContext {{ return [pscustomobject]@{{ Subscription = [pscustomobject]@{{ Id = '00000000-0000-4000-8000-000000000305' }}; Tenant = [pscustomobject]@{{ Id = '00000000-0000-4000-8000-000000000306' }} }} }}
function global:Get-AzResource {{ [CmdletBinding()] param([string]$ResourceId) return [pscustomobject]@{{ ResourceId = $ResourceId; Tags = [ordered]@{{ purpose = 'az305-lab'; labId = '__LAB_ID__'; runId = $env:AZ305_TEST_RUN_ID; expiresOn = '2099-12-31' }} }} }}
function global:Remove-AzResource {{ [CmdletBinding()] param([string]$ResourceId, [switch]$Force) Add-Content -LiteralPath $env:AZ305_TEST_CALL_LOG -Value $ResourceId; return $true }}
'@.Replace('__LAB_ID__', '{lab['id']}')
    }}

    function Get-CleanupFailureShim {{
        if ($IsCliTrack) {{
            return $ShimPreamble + @'
function global:az {{
    if ($args[0] -eq 'account' -and $args[1] -eq 'show') {{ $global:LASTEXITCODE = 0; return '{{"id":"00000000-0000-4000-8000-000000000305","tenantId":"00000000-0000-4000-8000-000000000306"}}' }}
    $idIndex = [Array]::IndexOf([object[]]$args, '--ids')
    $id = [string]$args[$idIndex + 1]
    if ($args[0] -eq 'resource' -and $args[1] -eq 'show') {{ $global:LASTEXITCODE = 0; return ([ordered]@{{ id = $id; tags = [ordered]@{{ purpose = 'az305-lab'; labId = '__LAB_ID__'; runId = $env:AZ305_TEST_RUN_ID; expiresOn = '2099-12-31' }} }} | ConvertTo-Json -Compress) }}
    if ($args[0] -eq 'resource' -and $args[1] -eq 'delete') {{ Record-Az305TestCall -Name 'delete-failure'; $global:LASTEXITCODE = 17; return }}
    throw 'Unexpected Azure CLI cleanup command.'
}}
'@.Replace('__LAB_ID__', '{lab['id']}')
        }}
        return $ShimPreamble + @'
function global:Get-AzContext {{ return [pscustomobject]@{{ Subscription = [pscustomobject]@{{ Id = '00000000-0000-4000-8000-000000000305' }}; Tenant = [pscustomobject]@{{ Id = '00000000-0000-4000-8000-000000000306' }} }} }}
function global:Get-AzResource {{ [CmdletBinding()] param([string]$ResourceId) return [pscustomobject]@{{ ResourceId = $ResourceId; Tags = [ordered]@{{ purpose = 'az305-lab'; labId = '__LAB_ID__'; runId = $env:AZ305_TEST_RUN_ID; expiresOn = '2099-12-31' }} }} }}
function global:Remove-AzResource {{ [CmdletBinding()] param([string]$ResourceId, [switch]$Force) Record-Az305TestCall -Name 'Remove-AzResource-failure'; throw 'Injected delete failure.' }}
'@.Replace('__LAB_ID__', '{lab['id']}')
    }}
    }}

    It 'uses exactly one generated region in every lifecycle script' {{
        Get-ChildItem $ScriptRoot -Filter '*.ps1' | ForEach-Object {{
            $marker = 'BEGIN GENERATED ' + 'AZ305 V1'
            (Get-Content $_.FullName -Raw).Split($marker).Count | Should -Be 2
        }}
    }}

    It 'executes setup preview without cloud access and uses only the Golden Lab intent record' {{
        $run = 'preview-000001'
        $result = Invoke-LifecycleProcess -ScriptName 'Setup.ps1' -Parameters (Get-TestParameterSet -RunId $run) -ShimBody $OfflineRefusalShim
        $result.ExitCode | Should -Be 0
        $statePath = Join-Path $IsolatedLab ".state/$run/run.json"
        if ($IsFoundationPreview) {{
            $state = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
            $state.status | Should -Be 'planned'
            $state.execute | Should -BeFalse
        }} else {{ Test-Path $statePath | Should -BeFalse }}
        Test-Path $CallLog | Should -BeFalse
    }}

    It 'refuses a mismatched context and keeps every design simulation offline' {{
        $run = 'context-000001'
        $shim = if ($IsDesignSimulation) {{ $OfflineRefusalShim }} else {{ $ContextMismatchShim }}
        $result = Invoke-LifecycleProcess -ScriptName 'Setup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $shim
        if ($IsDesignSimulation) {{
            $result.ExitCode | Should -BeIn @(0, 1, 2)
            Test-Path $CallLog | Should -BeFalse
            if ($SetupHasDesignCloudGate) {{
                $result.ExitCode | Should -Be 2
                Test-Path (Join-Path $IsolatedLab ".state/$run") | Should -BeFalse
            }}
        }} else {{
            $result.ExitCode | Should -Be 2
            Test-Path (Join-Path $IsolatedLab ".state/$run") | Should -BeFalse
            Test-Path $CallLog | Should -BeFalse
        }}
    }}

    It 'writes recovery state before an injected checkpoint failure and preserves failed status' {{
        if ($IsDesignSimulation) {{
            (Get-Content (Join-Path $ScriptRoot 'Setup.ps1') -Raw).IndexOf('Save-RunState -State $state') | Should -BeLessThan (Get-Content (Join-Path $ScriptRoot 'Setup.ps1') -Raw).IndexOf('# {lab['number']}-CP01:')
            return
        }}
        $run = 'failure-000001'
        $result = Invoke-LifecycleProcess -ScriptName 'Setup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $MatchingFailureShim
        $result.ExitCode | Should -Be 1
        $calls = @(Get-Content -LiteralPath $CallLog)
        $calls.Count | Should -BeGreaterThan 0
        $calls[0] | Should -Match 'state=True'
        $state = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/run.json") -Raw | ConvertFrom-Json
        $state.status | Should -Be 'failed'
    }}

    It 'never overwrites an existing recovery record' {{
        $run = 'existing-000001'
        $statePath = Write-TestRunState -RunId $run -Status deployed
        $before = Get-Content -LiteralPath $statePath -Raw
        $shim = if ($IsDesignSimulation) {{ $OfflineRefusalShim }} else {{ $MatchingFailureShim }}
        $result = Invoke-LifecycleProcess -ScriptName 'Setup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $shim
        $result.ExitCode | Should -Be 2
        (Get-Content -LiteralPath $statePath -Raw) | Should -BeExactly $before
        Test-Path $CallLog | Should -BeFalse
    }}

    It 'fails deployment validation for a failed setup state without cloud access' {{
        $run = 'validate-failed-000001'
        Write-TestRunState -RunId $run -Status failed | Out-Null
        $result = Invoke-LifecycleProcess -ScriptName 'Validate.ps1' -Parameters (Get-TestParameterSet -RunId $run -Mode Deployment) -ShimBody $OfflineRefusalShim
        $result.ExitCode | Should -Be 1
        $artifact = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/validation.json") -Raw | ConvertFrom-Json
        $artifact.result | Should -Be 'fail'
        Test-Path $CallLog | Should -BeFalse
    }}

    It 'executes every positive and negative checkpoint independently or gates design cloud validation' {{
        $run = 'validate-live-000001'
        Write-TestRunState -RunId $run | Out-Null
        $shim = if ($IsDesignSimulation) {{ $OfflineRefusalShim }} else {{ $MatchingFailureShim }}
        $result = Invoke-LifecycleProcess -ScriptName 'Validate.ps1' -Parameters (Get-TestParameterSet -RunId $run -Mode Deployment -Execute) -ShimBody $shim
        $artifact = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/validation.json") -Raw | ConvertFrom-Json
        if ($ValidationHasDesignCloudGate) {{
            $result.ExitCode | Should -Be 2
            $artifact.result | Should -Be 'partial'
            Test-Path $CallLog | Should -BeFalse
        }} else {{
            $result.ExitCode | Should -BeIn @(0, 1)
            @($artifact.assertions | Where-Object id -Match '^LAB{lab['number']}-CP0[1-5]-(POS|NEG)$').Count | Should -Be 10
        }}
    }}

    It 'refuses a recorded ownership mismatch before any live inspection or deletion' {{
        $run = 'ownership-000001'
        $id = "/subscriptions/$SubscriptionId/resourceGroups/rg-az305-contract/providers/Microsoft.Test/parents/one"
        Write-TestRunState -RunId $run -ManagedObjects @((Get-ManagedObjectFixture -Id $id -RunId $run -RecordedRunId 'foreign-run')) | Out-Null
        $result = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $OfflineRefusalShim
        $result.ExitCode | Should -Be 1
        Test-Path $CallLog | Should -BeFalse
        $artifact = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/cleanup.json") -Raw | ConvertFrom-Json
        $artifact.ownershipVerified | Should -BeFalse
        $artifact.actions[0].result | Should -Be 'refused'
    }}

    It 'keeps a failed deletion recoverable and prevents design-simulation cloud cleanup' {{
        $run = 'delete-failed-000001'
        $id = "/subscriptions/$SubscriptionId/resourceGroups/rg-az305-contract/providers/Microsoft.Test/parents/one"
        Write-TestRunState -RunId $run -ManagedObjects @((Get-ManagedObjectFixture -Id $id -RunId $run)) | Out-Null
        $shim = if ($IsDesignSimulation) {{ $OfflineRefusalShim }} else {{ Get-CleanupFailureShim }}
        $result = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $shim
        $result.ExitCode | Should -Be 1
        $state = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/run.json") -Raw | ConvertFrom-Json
        @($state.managedObjects).Count | Should -Be 1
        if ($IsDesignSimulation) {{ Test-Path $CallLog | Should -BeFalse }} else {{ $state.status | Should -Be 'failed' }}
    }}

    It 'cleans in reverse dependency order and is idempotent' {{
        $run = 'cleanup-order-000001'
        if ($IsDesignSimulation) {{
            Write-TestRunState -RunId $run | Out-Null
            $first = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $OfflineRefusalShim
            $second = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $OfflineRefusalShim
            $first.ExitCode | Should -Be 0
            $second.ExitCode | Should -Be 0
            Test-Path $CallLog | Should -BeFalse
            return
        }}
        $parentId = "/subscriptions/$SubscriptionId/resourceGroups/rg-az305-contract/providers/Microsoft.Test/parents/one"
        $childId = "$parentId/children/two"
        $objects = @((Get-ManagedObjectFixture -Id $parentId -RunId $run), (Get-ManagedObjectFixture -Id $childId -RunId $run))
        $originals = @([pscustomobject]@{{ id = $childId; setting = 'synthetic-original'; value = 'before' }})
        Write-TestRunState -RunId $run -ManagedObjects $objects -OriginalSettings $originals | Out-Null
        $first = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody (Get-CleanupSuccessShim)
        $first.ExitCode | Should -Be 0
        @(Get-Content -LiteralPath $CallLog) | Should -Be @($childId, $parentId)
        $state = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/run.json") -Raw | ConvertFrom-Json
        $state.status | Should -Be 'cleaned'
        @($state.managedObjects).Count | Should -Be 0
        @($state.originalSettings).Count | Should -Be 0
        $second = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $OfflineRefusalShim
        $second.ExitCode | Should -Be 0
        @(Get-Content -LiteralPath $CallLog).Count | Should -Be 2
    }}

    It 'passes post-cleanup validation only after actual zero-residual cleanup' {{
        $run = 'post-cleanup-000001'
        Write-TestRunState -RunId $run | Out-Null
        (Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $OfflineRefusalShim).ExitCode | Should -Be 0
        $result = Invoke-LifecycleProcess -ScriptName 'Validate.ps1' -Parameters (Get-TestParameterSet -RunId $run -Mode PostCleanup) -ShimBody $OfflineRefusalShim
        $result.ExitCode | Should -Be 0
        $artifact = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/validation.json") -Raw | ConvertFrom-Json
        $artifact.result | Should -Be 'pass'
    }}
{partial_deployment_test}
}}
"""


def fixture_json(kind: str, lab: dict[str, Any]) -> str:
    run_id = f"synthetic-{lab['number']}0001"
    if kind == "run":
        value = {"schemaVersion": "1.0.0", "labId": lab["id"], "runId": run_id, "track": lab["track"], "implementationMode": lab["implementationMode"], "status": "planned" if lab["implementationMode"] == "design-simulation" or lab["id"] in {"LAB-21", "LAB-26"} else "deployed", "createdAt": "2026-09-02T00:00:00Z", "execute": True, "parameters": {"location": "westeurope", "secondaryLocation": "northeurope", "resourceGroup": f"rg-az305-{run_id}"}, "managedObjects": [], "originalSettings": []}
    elif kind == "validation":
        value = {"schemaVersion": "1.0.0", "labId": lab["id"], "runId": run_id, "mode": "PostCleanup", "result": "pass", "validatedAt": "2026-09-02T00:00:00Z", "assertions": [{"id": f"LAB{lab['number']}-FIX-POS", "kind": "positive", "passed": True, "message": "Synthetic cleanup fixture is schema valid."}, {"id": f"LAB{lab['number']}-FIX-NEG", "kind": "negative", "passed": True, "message": "Synthetic fixture records no active managed object."}]}
    else:
        value = {"schemaVersion": "1.0.0", "labId": lab["id"], "runId": run_id, "result": "pass", "completedAt": "2026-09-02T00:00:00Z", "ownershipVerified": True, "activeManagedObjects": 0, "actions": []}
    raw = json.dumps(value, indent=2)
    lines = raw.splitlines()
    lines.insert(1, '  "_generatedBegin": "BEGIN GENERATED AZ305 V1",')
    lines.insert(-1, '  ,"_generatedEnd": "END GENERATED AZ305 V1"')
    return "\n".join(lines) + "\n"


def bicep(lab: dict[str, Any]) -> str:
    number = lab["number"]
    if number == "18":
        body = """targetScope = 'resourceGroup'
param location string = resourceGroup().location
@minLength(6)
@maxLength(64)
param runId string
param expiresOn string
param controlVmSku string = 'Standard_D2s_v5'
param workerVmSku string = 'Standard_D2s_v5'
param adminUsername string = 'az305admin'
param adminSshPublicKey string
var suffix = uniqueString(resourceGroup().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-18', runId: runId, expiresOn: expiresOn }
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-compute-${suffix}'
  location: location
  tags: tags
}
resource network 'Microsoft.Network/virtualNetworks@2024-05-01' = {
  name: 'vnet-az305-${suffix}'
  location: location
  tags: tags
  properties: { addressSpace: { addressPrefixes: ['10.18.0.0/16'] }, subnets: [{ name: 'compute', properties: { addressPrefix: '10.18.1.0/24' } }] }
}
resource batch 'Microsoft.Batch/batchAccounts@2024-07-01' = {
  name: 'batch${suffix}'
  location: location
  tags: tags
  identity: { type: 'SystemAssigned' }
  properties: { poolAllocationMode: 'BatchService', publicNetworkAccess: 'Disabled' }
}
resource batchPool 'Microsoft.Batch/batchAccounts/pools@2024-07-01' = {
  parent: batch
  name: 'pool-${suffix}'
  tags: tags
  properties: {
    vmSize: workerVmSku
    deploymentConfiguration: {
      virtualMachineConfiguration: {
        imageReference: { publisher: 'Canonical', offer: 'ubuntu-24_04-lts', sku: 'server', version: 'latest' }
        nodeAgentSkuId: 'batch.node.ubuntu 24.04'
      }
    }
    networkConfiguration: {
      subnetId: resourceId('Microsoft.Network/virtualNetworks/subnets', network.name, 'compute')
      publicIPAddressConfiguration: { provision: 'NoPublicIPAddresses' }
    }
    scaleSettings: { fixedScale: { targetDedicatedNodes: 0, targetLowPriorityNodes: 0, resizeTimeout: 'PT15M' } }
    taskSlotsPerNode: 1
    interNodeCommunication: 'Disabled'
  }
}
resource controlScaleSet 'Microsoft.Compute/virtualMachineScaleSets@2024-11-01' = {
  name: 'vmss-control-${suffix}'
  location: location
  tags: tags
  sku: { name: controlVmSku, tier: 'Standard', capacity: 0 }
  identity: { type: 'UserAssigned', userAssignedIdentities: { '${identity.id}': {} } }
  zones: ['1', '2', '3']
  properties: {
    orchestrationMode: 'Flexible'
    platformFaultDomainCount: 1
    zoneBalance: true
    upgradePolicy: { mode: 'Manual' }
    virtualMachineProfile: {
      osProfile: {
        computerNamePrefix: 'ctrl-${suffix}'
        adminUsername: adminUsername
        linuxConfiguration: {
          disablePasswordAuthentication: true
          provisionVMAgent: true
          ssh: { publicKeys: [{ path: '/home/${adminUsername}/.ssh/authorized_keys', keyData: adminSshPublicKey }] }
        }
      }
      storageProfile: {
        imageReference: { publisher: 'Canonical', offer: 'ubuntu-24_04-lts', sku: 'server', version: 'latest' }
        osDisk: { createOption: 'FromImage', caching: 'ReadWrite', managedDisk: { storageAccountType: 'Standard_LRS' } }
      }
      networkProfile: {
        networkInterfaceConfigurations: [{
          name: 'private-nic'
          properties: {
            primary: true
            enableIPForwarding: false
            ipConfigurations: [{ name: 'private-ip', properties: { primary: true, subnet: { id: resourceId('Microsoft.Network/virtualNetworks/subnets', network.name, 'compute') } } }]
          }
        }]
      }
      securityProfile: { securityType: 'TrustedLaunch', uefiSettings: { secureBootEnabled: true, vTpmEnabled: true } }
    }
  }
}
output cleanupResourceIds array = [network.id, identity.id, batch.id, batchPool.id, controlScaleSet.id]
output topology object = {
  batchAccountName: batch.name
  batchPoolName: batchPool.name
  boundedWorkerCapacity: 0
  boundedControlCapacity: 0
  vmAvailabilityModel: 'three-zone-capable'
  scalePrerequisite: 'Validate current image/SKU support and add explicit NAT or inspected firewall egress before raising either capacity above zero.'
}
"""
    elif number == "21":
        body = """targetScope = 'resourceGroup'
param location string = resourceGroup().location
@minLength(6)
@maxLength(64)
param runId string
param expiresOn string
var suffix = uniqueString(resourceGroup().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-21', runId: runId, expiresOn: expiresOn }
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-delivery-${suffix}'
  location: location
  tags: tags
}
resource appConfiguration 'Microsoft.AppConfiguration/configurationStores@2024-05-01' = {
  name: 'appcs${suffix}'
  location: location
  tags: tags
  sku: { name: 'free' }
  identity: { type: 'UserAssigned', userAssignedIdentities: { '${identity.id}': {} } }
  properties: { disableLocalAuth: true, publicNetworkAccess: 'Disabled' }
}
resource managedRedis 'Microsoft.Cache/redisEnterprise@2025-07-01' = {
  name: 'redis-${suffix}'
  location: location
  tags: tags
  sku: { name: 'Balanced_B0' }
  identity: { type: 'UserAssigned', userAssignedIdentities: { '${identity.id}': {} } }
  properties: { encryption: {}, highAvailability: 'Disabled', minimumTlsVersion: '1.2', publicNetworkAccess: 'Disabled' }
}
resource managedRedisDatabase 'Microsoft.Cache/redisEnterprise/databases@2025-07-01' = {
  parent: managedRedis
  name: 'default'
  properties: { clientProtocol: 'Encrypted', clusteringPolicy: 'OSSCluster', evictionPolicy: 'VolatileLRU', modules: [], port: 10000 }
}
output deliveryResourceIds array = [identity.id, appConfiguration.id, managedRedis.id, managedRedisDatabase.id]
output deploymentMode object = {
  mode: 'what-if-only-safe-analogue'
  highAvailability: 'intentionally-disabled'
  publicNetworkAccess: 'disabled-on-both-service-parents'
  privateAccess: 'private endpoints and DNS are intentionally omitted and must be designed before any live client use'
  untaggableChildResourceIds: [managedRedisDatabase.id]
}
"""
    elif number == "26":
        body = """targetScope = 'subscription'
param location string = 'westeurope'
param secondaryLocation string = 'northeurope'
param runId string
param expiresOn string
var suffix = uniqueString(subscription().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-26', runId: runId, expiresOn: expiresOn }
resource primaryGroup 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-platform-${runId}-primary'
  location: location
  tags: tags
}
resource secondaryGroup 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-platform-${runId}-secondary'
  location: secondaryLocation
  tags: tags
}
resource globalGroup 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-platform-${runId}-global'
  location: location
  tags: tags
}
module primary 'modules/regional-stamp.bicep' = { name: 'primary-${suffix}', scope: primaryGroup, params: { location: location, runId: runId, stamp: 'primary', expiresOn: expiresOn } }
module secondary 'modules/regional-stamp.bicep' = { name: 'secondary-${suffix}', scope: secondaryGroup, params: { location: secondaryLocation, runId: runId, stamp: 'secondary', expiresOn: expiresOn } }
module globalEntry 'modules/global-entry.bicep' = { name: 'global-${suffix}', scope: globalGroup, params: { location: location, runId: runId, expiresOn: expiresOn } }
output cleanupResourceIds array = concat(
  [primaryGroup.id],
  primary.outputs.stampResourceIds,
  [secondaryGroup.id],
  secondary.outputs.stampResourceIds,
  [globalGroup.id],
  globalEntry.outputs.globalResourceIds
)
output referenceBoundary object = {
  implementationMode: 'what-if-only-safe-analogue'
  productionReady: false
  omittedCapabilities: [
    'application compute and regional ingress'
    'relational data and cross-region data replication'
    'Azure Managed Redis databases'
    'DCR associations, diagnostic settings, and alert rules'
    'Front Door origins, origin groups, routes, WAF policy, and custom domains'
    'private endpoints, Standard Load Balancer, and explicit NAT or inspected-firewall egress'
  ]
}
"""
    else:
        body = """targetScope = 'subscription'
param location string = 'westeurope'
param secondaryLocation string
param runId string
param expiresOn string
var suffix = uniqueString(subscription().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-27', runId: runId, expiresOn: expiresOn }
resource hybridGroup 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-hybrid-${runId}'
  location: location
  tags: tags
}
module foundation 'modules/hybrid-foundation.bicep' = {
  name: 'hybrid-foundation-${suffix}'
  scope: hybridGroup
  params: { location: location, secondaryLocation: secondaryLocation, runId: runId, expiresOn: expiresOn }
}
output migrationPlan object = {
  mode: 'offline-simulation'
  primaryRegion: location
  secondaryRegion: secondaryLocation
  ownership: tags
  waves: ['foundation', 'low-risk', 'data-modernization', 'critical-workloads']
  rollbackRequired: true
  taggedFoundationResourceIds: concat([hybridGroup.id], foundation.outputs.taggedFoundationResourceIds)
  untaggableIllustrativeResourceIds: foundation.outputs.untaggableIllustrativeResourceIds
  ownershipException: 'Policy assignments do not support resource tags; this template is compile-only and no deployment or cleanup path is provided.'
}
"""
    return body


def params_json(lab: dict[str, Any]) -> str:
    parameters = {"runId": {"value": f"synthetic-{lab['number']}0001"}, "expiresOn": {"value": "2000-01-01"}}
    if lab["number"] == "18":
        parameters.update({
            "controlVmSku": {"value": "Standard_D2s_v5"},
            "workerVmSku": {"value": "Standard_D2s_v5"},
            "adminUsername": {"value": "az305admin"},
            "adminSshPublicKey": {
                "value": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC+wWK73dCr+jgQOAxNsHAnNNNMEMWOHYEccp6wJm2gotpr9katuF/ZAdou5AaW1C61slRkHRkpRRX9FA9CYBiitZgvCCz+3nWNN7l/Up54Zps/pHWGZLHNJZRYyAB6j5yVLMVHIHriY49d/GZTZVNB8GoJv9Gakwc/fuEZYYl4YDFiGMBP///TzlI4jhiJzjKnEvqPFki5p2ZRJqcbCiF4pJrxUQR/RXqVFQdbRLZgYfJ8xGB878RENq3yQ39d8dVOkq4edbkzwcUmwwwkYVPIoDGsYLaRHnG+To7FvMeyO7xDVQkMKzopTQV8AuKpyvpqu0a9pWOMaiCyDytO7GGN az305@example.invalid"
            },
        })
    if lab["number"] == "27":
        parameters.update({"location": {"value": "westeurope"}, "secondaryLocation": {"value": "northeurope"}})
    return json.dumps({"$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#", "contentVersion": "1.0.0.0", "parameters": parameters}, indent=2) + "\n"


def lab_catalog_markdown(catalog: dict[str, Any]) -> str:
    lines = [
        "# Lab catalog", "",
        "Every folder is portable and offline-testable. Preview is the default; a live path requires explicit execution and acknowledgement gates.", "",
        "| Lab | Title | Domain | Lane | Mode | Objectives | Questions |", "| --- | --- | --- | --- | --- | --- | ---: |",
    ]
    for lab in catalog["labs"]:
        objectives = ", ".join(f"`{item}`" for item in lab["primaryObjectiveIds"])
        if lab["reinforcesAllOfficialObjectives"]:
            objectives = "Reinforces all 49"
        lines.append(
            f"| [{lab['id']}]({lab['folder']}/README.md) | {lab['title']} | {lab['domainId']} | {lab['laneLabel']} | "
            f"`{lab['implementationMode']}` | {objectives} | {lab['questionCount']} |"
        )
    lines.extend(["", "The scored assessment total is exactly 1,250 questions across Labs 01–25. Answer keys are intentionally excluded from the searchable documentation site."])
    return "\n".join(lines) + "\n"


def supporting_artifacts(lab: dict[str, Any]) -> dict[str, str]:
    number = lab["number"]
    synthetic_subscription = "00000000-0000-0000-0000-000000000305"
    if number == "01":
        return {"artifacts/dcr.json": json.dumps({
            "location": "westeurope",
            "properties": {
                "dataSources": {"performanceCounters": [{"name": "baseline", "streams": ["Microsoft-Perf"], "samplingFrequencyInSeconds": 60, "counterSpecifiers": ["\\Processor(_Total)\\% Processor Time"]}]},
                "destinations": {"logAnalytics": [{"name": "regional", "workspaceResourceId": f"/subscriptions/{synthetic_subscription}/resourceGroups/rg-synthetic/providers/Microsoft.OperationalInsights/workspaces/log-synthetic"}]},
                "dataFlows": [{"streams": ["Microsoft-Perf"], "destinations": ["regional"]}],
            },
        }, indent=2) + "\n"}
    if number == "10":
        return {"artifacts/indexing-policy.json": json.dumps({
            "indexingMode": "consistent", "automatic": True,
            "includedPaths": [{"path": "/*"}],
            "excludedPaths": [{"path": "/largePayload/?"}],
            "compositeIndexes": [[{"path": "/tenantId", "order": "ascending"}, {"path": "/eventTime", "order": "descending"}]],
        }, indent=2) + "\n"}
    if number == "12":
        return {"artifacts/lifecycle-policy.json": json.dumps({
            "rules": [{"enabled": True, "name": "tier-then-expire", "type": "Lifecycle", "definition": {"filters": {"blobTypes": ["blockBlob"], "prefixMatch": ["evidence/"]}, "actions": {"baseBlob": {"tierToCool": {"daysAfterModificationGreaterThan": 30}, "tierToArchive": {"daysAfterModificationGreaterThan": 180}, "delete": {"daysAfterModificationGreaterThan": 2555}}}}}],
        }, indent=2) + "\n"}
    if number == "13":
        return {"artifacts/pipeline.json": json.dumps({
            "name": "pl_synthetic_incremental_ingestion",
            "properties": {"parameters": {"windowStart": {"type": "String"}, "windowEnd": {"type": "String"}}, "activities": [{"name": "CopyBoundedWindow", "type": "Copy", "policy": {"timeout": "0.01:00:00", "retry": 2}, "inputs": [], "outputs": []}], "annotations": ["synthetic", "offline-authored"]},
        }, indent=2) + "\n"}
    if number == "22":
        portfolio = (
            "applicationId,owner,businessCriticality,environment,hosting,operatingSystem,dataClassification,monthlyCost,disposition,wave,supportStatus,exceptionId\n"
            "APP-001,finance-platform,tier-1,production,vm,linux,confidential,4200,replatform,2,supported,\n"
            "APP-002,commerce-platform,tier-1,production,physical,windows,restricted,6900,refactor,3,supported,\n"
            "APP-003,workplace,tier-3,development,vm,linux,internal,350,retire,1,unsupported,EXC-SYNTHETIC-01\n"
            "APP-004,data-platform,tier-2,production,vm,windows,confidential,2400,rehost,2,supported,\n"
        )
        dependencies = (
            "sourceApplicationId,targetApplicationId,protocol,criticality\n"
            "APP-001,APP-004,TDS,required\n"
            "APP-002,APP-001,HTTPS,required\n"
            "APP-003,APP-002,SFTP,optional\n"
        )
        return {"artifacts/portfolio.csv": portfolio, "artifacts/dependencies.csv": dependencies}
    if number == "26":
        regional_module = """targetScope = 'resourceGroup'
param location string
param runId string
param stamp string
param expiresOn string
var suffix = uniqueString(resourceGroup().id, runId, stamp)
var tags = { purpose: 'az305-lab', labId: 'LAB-26', runId: runId, expiresOn: expiresOn, stamp: stamp }
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = { name: 'id-${stamp}-${suffix}', location: location, tags: tags }
resource network 'Microsoft.Network/virtualNetworks@2024-05-01' = { name: 'vnet-${stamp}-${suffix}', location: location, tags: tags, properties: { addressSpace: { addressPrefixes: [stamp == 'primary' ? '10.26.0.0/16' : '10.27.0.0/16'] }, subnets: [{ name: 'private', properties: { addressPrefix: stamp == 'primary' ? '10.26.1.0/24' : '10.27.1.0/24' } }] } }
#disable-next-line BCP187
resource workspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = { name: 'log-${stamp}-${suffix}', location: location, tags: tags, properties: { retentionInDays: 30, features: { enableLogAccessUsingOnlyResourcePermissions: true } }, sku: { name: 'PerGB2018' } }
resource dcr 'Microsoft.Insights/dataCollectionRules@2023-03-11' = { name: 'dcr-${stamp}-${suffix}', location: location, tags: tags, properties: { dataSources: {}, destinations: { logAnalytics: [{ workspaceResourceId: workspace.id, name: 'regional' }] }, dataFlows: [] } }
resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = { name: 'st${suffix}', location: location, tags: tags, sku: { name: 'Standard_LRS' }, kind: 'StorageV2', properties: { allowBlobPublicAccess: false, minimumTlsVersion: 'TLS1_2', supportsHttpsTrafficOnly: true, publicNetworkAccess: 'Disabled' } }
resource documents 'Microsoft.DocumentDB/databaseAccounts@2024-11-15' = { name: 'cosmos-${stamp}-${suffix}', location: location, tags: tags, kind: 'GlobalDocumentDB', properties: { databaseAccountOfferType: 'Standard', capabilities: [{ name: 'EnableServerless' }], consistencyPolicy: { defaultConsistencyLevel: 'Session' }, locations: [{ locationName: location, failoverPriority: 0, isZoneRedundant: false }], publicNetworkAccess: 'Disabled', disableLocalAuth: true } }
resource messaging 'Microsoft.ServiceBus/namespaces@2024-01-01' = { name: 'sb-${stamp}-${suffix}', location: location, tags: tags, sku: { name: 'Basic', tier: 'Basic' }, properties: { minimumTlsVersion: '1.2', publicNetworkAccess: 'Disabled', disableLocalAuth: true } }
output stampResourceIds array = [identity.id, network.id, workspace.id, dcr.id, storage.id, documents.id, messaging.id]
"""
        global_module = """targetScope = 'resourceGroup'
param location string
param runId string
param expiresOn string
var suffix = uniqueString(resourceGroup().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-26', runId: runId, expiresOn: expiresOn }
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = { name: 'id-global-${suffix}', location: location, tags: tags }
resource frontDoor 'Microsoft.Cdn/profiles@2024-09-01' = { name: 'afd-${suffix}', location: 'global', tags: tags, sku: { name: 'Standard_AzureFrontDoor' } }
resource endpoint 'Microsoft.Cdn/profiles/afdEndpoints@2024-09-01' = { parent: frontDoor, name: 'entry-${suffix}', location: 'global', tags: tags, properties: { enabledState: 'Disabled' } }
output globalResourceIds array = [identity.id, frontDoor.id, endpoint.id]
"""
        assertions = [
            {"id": f"REG-{index:02d}", "domain": domain, "polarity": polarity, "expected": expected, "simulatedActual": expected}
            for index, (domain, polarity, expected) in enumerate([
                ("identity", "positive", "managed-identity-authorized"), ("global-routing", "positive", "healthy-region-selected"),
                ("regional-ingress", "negative", "failed-region-not-routed"), ("messaging", "positive", "buffer-preserved"),
                ("cache", "negative", "source-of-truth-remains-available"), ("data", "positive", "bounded-consistency-preserved"),
                ("capacity", "positive", "degraded-capacity-within-slo"), ("monitoring", "positive", "incident-signal-raised"),
                ("business", "positive", "checkout-path-available"), ("rollback", "negative", "no-automatic-purge"),
            ], 1)
        ]
        return {
            "artifacts/modules/regional-stamp.bicep": regional_module,
            "artifacts/modules/global-entry.bicep": global_module,
            "tests/fixtures/regional-failure.json": json.dumps({"fixtureType": "offline-regional-failure-simulation", "synthetic": True, "assertions": assertions}, indent=2) + "\n",
        }
    if number == "27":
        foundation_module = """targetScope = 'resourceGroup'
param location string
param secondaryLocation string
param runId string
param expiresOn string
var suffix = uniqueString(resourceGroup().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-27', runId: runId, expiresOn: expiresOn, simulation: 'offline' }
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = { name: 'id-hybrid-${suffix}', location: location, tags: tags }
resource network 'Microsoft.Network/virtualNetworks@2024-05-01' = { name: 'vnet-hybrid-${suffix}', location: location, tags: tags, properties: { addressSpace: { addressPrefixes: ['10.27.0.0/16'] }, subnets: [{ name: 'gateway', properties: { addressPrefix: '10.27.0.0/27' } }, { name: 'workloads', properties: { addressPrefix: '10.27.1.0/24' } }] } }
resource privateDns 'Microsoft.Network/privateDnsZones@2024-06-01' = { name: 'migration.az305.invalid', location: 'global', tags: tags }
#disable-next-line BCP187
resource workspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = { name: 'log-hybrid-${suffix}', location: location, tags: tags, properties: { retentionInDays: 30, features: { enableLogAccessUsingOnlyResourcePermissions: true } }, sku: { name: 'PerGB2018' } }
resource dcr 'Microsoft.Insights/dataCollectionRules@2023-03-11' = { name: 'dcr-hybrid-${suffix}', location: location, tags: tags, properties: { dataSources: {}, destinations: { logAnalytics: [{ workspaceResourceId: workspace.id, name: 'hybrid' }] }, dataFlows: [] } }
resource policy 'Microsoft.Authorization/policyAssignments@2024-04-01' = { name: guid(resourceGroup().id, 'az305-hybrid-policy', runId), properties: { displayName: 'AZ-305 synthetic hybrid guardrails', enforcementMode: 'DoNotEnforce', policyDefinitionId: '/providers/Microsoft.Authorization/policyDefinitions/1a4e592a-6a6e-44a5-9814-e36264ca96e7', nonComplianceMessages: [{ message: 'Offline simulation: review migration target compliance.' }] } }
output taggedFoundationResourceIds array = [identity.id, network.id, privateDns.id, workspace.id, dcr.id]
output untaggableIllustrativeResourceIds array = [policy.id]
output coexistence object = { secondaryRegion: secondaryLocation, connectivity: 'private-circuit-with-vpn-fallback', identity: 'managed-and-federated', monitoring: 'AMA-with-DCR' }
"""
        portfolio = (
            "applicationId,owner,disposition,wave,targetConcept,coexistenceBridge,rollback,decommissionGate\n"
            "HYB-001,finance,replatform,2,managed-relational,private-dns-bridge,restore-original-endpoint,business-reconciliation\n"
            "HYB-002,operations,rehost,1,zone-aware-vm,vpn-route-bridge,restart-source-vm,thirty-day-observation\n"
            "HYB-003,digital,refactor,3,container-platform,api-facade,revert-routing-weight,error-budget-approval\n"
            "HYB-004,records,retain,4,hybrid-archive,read-only-gateway,no-cutover,retention-signoff\n"
        )
        dependencies = (
            "sourceApplicationId,targetApplicationId,criticality,coexistenceBridge\n"
            "HYB-001,HYB-002,hard,private-dns-bridge\n"
            "HYB-003,HYB-001,hard,api-facade\n"
            "HYB-004,HYB-001,soft,read-only-gateway\n"
        )
        scenarios = [
            {"id": f"INJECT-{index:02d}", "wave": (index % 4) + 1, "inject": inject, "expectedDecision": decision, "maximumDecisionMinutes": 30, "simulatedDecisionMinutes": 12 + index, "businessAssertion": "pass", "prohibitedOutcomeObserved": False, "containsAutomaticPurge": False, "rollbackAuthority": "migration-command"}
            for index, (inject, decision) in enumerate([
                ("discovery-collector-unavailable", "continue-from-signed-inventory"), ("private-circuit-loss", "use-tested-vpn-failover"),
                ("replication-lag-exceeds-rpo", "pause-cutover"), ("latest-recovery-point-corrupt", "select-last-verified-point"),
                ("policy-denies-target", "remediate-before-retry"), ("identity-provider-unavailable", "hold-privileged-cutover"),
                ("cutover-window-exceeded", "invoke-owned-rollback"), ("reconciliation-mismatch", "restore-source-authority"),
                ("decommission-request-early", "deny-until-observation-gate"),
            ], 1)
        ]
        report = {"status": "offline-validated", "lastLiveVerified": None, "assertions": [{"id": name, "result": "pass"} for name in ("schema", "traceability", "bicep", "fixtures", "security", "portability", "cleanup-plan")], "claims": ["Offline fixtures validated", "No cloud request performed", "Live verification remains unset"]}
        files = {
            "artifacts/modules/hybrid-foundation.bicep": foundation_module,
            "tests/fixtures/portfolio.csv": portfolio,
            "tests/fixtures/dependencies.csv": dependencies,
            "tests/fixtures/failure-scenarios.json": json.dumps(scenarios, indent=2) + "\n",
            "tests/fixtures/release-report.json": json.dumps(report, indent=2) + "\n",
        }
        fixture_files = {path: value for path, value in files.items() if path.startswith("tests/fixtures/")}
        manifest = {"schemaVersion": "1.0.0", "files": [{"path": path, "sha256": hashlib.sha256(value.encode("utf-8")).hexdigest()} for path, value in sorted(fixture_files.items())]}
        files["tests/fixtures/manifest.json"] = json.dumps(manifest, indent=2) + "\n"
        return files
    return {}


def generate(check: bool, only: set[str]) -> int:
    blueprint, catalog, content_model, _, _ = load_model()
    contents = {f"LAB-{str(item['number']).zfill(2)}": item for item in content_model["labs"]}
    objectives_by_id = objective_map(blueprint)
    drift: list[str] = []
    for lab in catalog["labs"]:
        if only and lab["id"] not in only:
            continue
        content = contents.get(lab["id"])
        if content is None or len(content.get("checkpoints", [])) != 5:
            raise ValueError(f"{lab['id']} must have substantive content and exactly five checkpoints")
        objectives = list(lab["primaryObjectiveIds"])
        if lab.get("reinforcesAllOfficialObjectives"):
            objectives = [item for item in objectives_by_id if not item.startswith("FD-")]
        requirements = requirement_document(lab, content, objectives)
        decision = decision_document(lab, content, objectives)
        metadata = lab_metadata(lab, content, objectives)
        scripts = {
            "Preflight.ps1": preflight_script(lab, content),
            "Setup.ps1": setup_script(lab, content),
            "Validate.ps1": validate_script(lab, content),
            "Cleanup.ps1": cleanup_script(lab, content),
        }
        folder = ROOT / "labs" / lab["folder"]
        outputs = [
            (folder / "lab.yml", yaml_text(metadata), "yaml"),
            (folder / "design/requirements.yml", yaml_text(requirements), "yaml"),
            (folder / "design/decision.yml", yaml_text(decision), "yaml"),
            (folder / "diagrams/architecture.mmd", architecture_mermaid(lab, content), "mermaid"),
            (folder / "README.md", readme(lab, content, objectives, requirements, decision, scripts, catalog), "markdown"),
            (folder / "solution/README.md", solution_readme(lab, content, decision), "markdown"),
            (folder / "tests/README.md", tests_readme(lab), "markdown"),
            (folder / "tests/Contract.Tests.ps1", pester_tests(lab, content), "powershell"),
        ]
        for name, script in scripts.items():
            outputs.append((folder / "scripts" / lab["track"] / name, script, "powershell"))
        for path, body, style in outputs:
            if write_or_check(path, body, style, check):
                drift.append(str(path.relative_to(ROOT)))
        fixtures = {"run": "run.sample.json", "validation": "validation.sample.json", "cleanup": "cleanup.sample.json"}
        for kind, filename in fixtures.items():
            path = folder / "tests/fixtures" / filename
            expected = fixture_json(kind, lab)
            actual = path.read_text(encoding="utf-8") if path.exists() else ""
            if actual != expected:
                drift.append(str(path.relative_to(ROOT)))
                if not check:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with path.open("w", encoding="utf-8", newline="\n") as handle:
                        handle.write(expected)
        if lab.get("supplementalBicep"):
            if write_or_check(folder / "artifacts/main.bicep", bicep(lab), "bicep", check):
                drift.append(str((folder / "artifacts/main.bicep").relative_to(ROOT)))
            parameters_path = folder / "artifacts/parameters.example.json"
            expected = params_json(lab)
            actual = parameters_path.read_text(encoding="utf-8") if parameters_path.exists() else ""
            if actual != expected:
                drift.append(str(parameters_path.relative_to(ROOT)))
                if not check:
                    parameters_path.parent.mkdir(parents=True, exist_ok=True)
                    with parameters_path.open("w", encoding="utf-8", newline="\n") as handle:
                        handle.write(expected)
        for relative, expected in supporting_artifacts(lab).items():
            artifact_path = folder / relative
            if artifact_path.suffix == ".bicep":
                if write_or_check(artifact_path, expected, "bicep", check):
                    drift.append(str(artifact_path.relative_to(ROOT)))
                continue
            actual = artifact_path.read_text(encoding="utf-8") if artifact_path.exists() else ""
            if actual != expected:
                drift.append(str(artifact_path.relative_to(ROOT)))
                if not check:
                    artifact_path.parent.mkdir(parents=True, exist_ok=True)
                    with artifact_path.open("w", encoding="utf-8", newline="\n") as handle:
                        handle.write(expected)
    if not only and write_or_check(ROOT / "labs/README.md", lab_catalog_markdown(catalog), "markdown", check):
        drift.append("labs/README.md")
    if drift:
        if check:
            print("Generated lab drift:\n" + "\n".join(f"- {item}" for item in drift))
            return 1
        print(f"updated {len(drift)} generated lab artifacts")
    else:
        print("generated lab artifacts are current")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Report drift without writing")
    parser.add_argument("--only", nargs="*", default=[], metavar="LAB-NN", help="Generate only selected lab IDs")
    args = parser.parse_args()
    only = set(args.only)
    unknown = only - {f"LAB-{index:02d}" for index in range(28)}
    if unknown:
        parser.error(f"Unknown lab IDs: {', '.join(sorted(unknown))}")
    return generate(args.check, only)


if __name__ == "__main__":
    raise SystemExit(main())
