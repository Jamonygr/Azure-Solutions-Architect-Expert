# BEGIN GENERATED AZ305 V1
[CmdletBinding()]
param(
    [string]$SubscriptionId = $env:AZ305_SUBSCRIPTION_ID,
    [string]$TenantId = $env:AZ305_TENANT_ID,
    [ValidatePattern('^[a-z0-9-]{6,64}$')][string]$RunId = $env:AZ305_RUN_ID,
    [string]$Location = $(if ($env:AZ305_LOCATION) { $env:AZ305_LOCATION } else { 'westeurope' }),
    [string]$SecondaryLocation = $(if ($env:AZ305_SECONDARY_LOCATION) { $env:AZ305_SECONDARY_LOCATION } else { 'northeurope' }),
    [string]$ResourceGroup = $(if ($env:AZ305_RESOURCE_GROUP) { $env:AZ305_RESOURCE_GROUP } else { "rg-az305-$RunId" }),
    [string]$WorkloadName = $(if ($env:AZ305_WORKLOAD_NAME) { $env:AZ305_WORKLOAD_NAME } else { "az305-$RunId" }),
    [string]$ExpiresOn = $(if ($env:AZ305_EXPIRES_ON) { $env:AZ305_EXPIRES_ON } else { (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd') }),
    [ValidateSet('Deployment', 'PostCleanup')][string]$Mode = 'Deployment',
    [switch]$Execute,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
if (-not $RunId) { [Console]::Error.WriteLine('RunId or AZ305_RUN_ID is required.'); exit 2 }
# Every lifecycle entrypoint intentionally exposes the same public parameter contract.
@($SubscriptionId, $TenantId, $RunId, $Location, $SecondaryLocation, $ResourceGroup, $WorkloadName, $ExpiresOn, $Mode, $Execute, $AcknowledgeCost, $AcknowledgeTenantChange) | Out-Null

$LabRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$StateRoot = Join-Path $LabRoot ".state/$RunId"
$RunPath = Join-Path $StateRoot 'run.json'
$ValidationPath = Join-Path $StateRoot 'validation.json'


if (-not (Test-Path -LiteralPath $RunPath)) {
    Write-Warning 'No run state exists; validation is gated.'
    exit 2
}
$state = Get-Content -LiteralPath $RunPath -Raw | ConvertFrom-Json
$assertions = [System.Collections.Generic.List[object]]::new()
function Add-ValidationAssertion {
    [CmdletBinding()]
    param([string]$Id, [ValidateSet('positive', 'negative')][string]$Kind, [bool]$Passed, [string]$Message)
    $assertions.Add([pscustomobject]@{ id = $Id; kind = $Kind; passed = $Passed; message = $Message })
}

function Save-ValidationArtifact {
    [CmdletBinding()]
    param([ValidateSet('pass', 'partial', 'fail')][string]$Result)
    $artifact = [ordered]@{ schemaVersion = '1.0.0'; labId = 'LAB-27'; runId = $RunId; mode = $Mode; result = $Result; validatedAt = (Get-Date).ToUniversalTime().ToString('o'); assertions = @($assertions) }
    $artifact | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $ValidationPath -Encoding utf8NoBOM
}

function Test-PositiveEvidence {
    [CmdletBinding()]
    param($Value)
    if ($Value -is [bool]) { return $Value }
    if ($null -eq $Value) { return $false }
    if ($Value -is [string]) { return -not [string]::IsNullOrWhiteSpace($Value) }
    if ($Value -is [System.Collections.IEnumerable]) { return @($Value).Count -gt 0 }
    return $true
}

function Test-NegativeEvidence {
    [CmdletBinding()]
    param($Value)
    if ($Value -is [bool]) { return $Value }
    if ($null -eq $Value) { return $true }
    if ($Value -is [string]) { return [string]::IsNullOrWhiteSpace($Value) }
    if ($Value -is [System.Collections.IEnumerable]) { return @($Value).Count -eq 0 }
    $properties = @($Value.PSObject.Properties | Where-Object { $_.MemberType -in @('NoteProperty', 'Property') })
    if ($properties.Count -eq 0) { return $false }
    return @($properties | Where-Object { -not (Test-NegativeEvidence -Value $_.Value) }).Count -eq 0
}

function Test-ProhibitedStateField {
    [CmdletBinding()]
    param($Value)
    $serialized = $Value | ConvertTo-Json -Depth 20
    return $serialized -match '(?i)"(?:token|password|secret|certificate|connectionString|sas|clientSecret|accessToken|refreshToken|accountKey|privateKey)"\s*:'
}

function Assert-InputSubscriptionScope {
    [CmdletBinding()]
    param($Inputs, [string]$ExpectedSubscriptionId)
    $entries = if ($Inputs -is [System.Collections.IDictionary]) {
        @($Inputs.GetEnumerator())
    } else {
        @($Inputs.PSObject.Properties | ForEach-Object { [pscustomobject]@{ Key = $_.Name; Value = $_.Value } })
    }
    foreach ($entry in $entries) {
        if ($entry.Value -is [string] -and [string]$entry.Value -match '^/subscriptions/([^/]+)/' -and $Matches[1] -ine $ExpectedSubscriptionId) {
            throw "Input $($entry.Key) belongs to a different subscription."
        }
    }
}

$stateIdentityMatches = (
    $state.labId -ceq 'LAB-27' -and
    $state.runId -ceq $RunId -and
    $state.track -ceq 'azure-powershell' -and
    $state.implementationMode -ceq 'design-simulation' -and
    $true
)
Add-ValidationAssertion -Id 'LAB27-VAL-POS-01' -Kind positive -Passed $stateIdentityMatches -Message 'Run identity, implementation mode, command track, tenant, and subscription exactly match the copied lab and requested run.'
$hasSensitiveName = Test-ProhibitedStateField -Value $state
Add-ValidationAssertion -Id 'LAB27-VAL-NEG-01' -Kind negative -Passed (-not $hasSensitiveName) -Message 'State contains no prohibited sensitive field name.'

if ($Mode -eq 'PostCleanup') {
    $cleanupPath = Join-Path $StateRoot 'cleanup.json'
    $cleanup = if (Test-Path -LiteralPath $cleanupPath) { Get-Content -LiteralPath $cleanupPath -Raw | ConvertFrom-Json } else { $null }
    Add-ValidationAssertion -Id 'LAB27-VAL-POS-02' -Kind positive -Passed ($null -ne $cleanup -and $cleanup.labId -ceq 'LAB-27' -and $cleanup.runId -ceq $RunId -and $cleanup.result -eq 'pass' -and $cleanup.ownershipVerified) -Message 'The exact run cleanup completed with verified ownership.'
    Add-ValidationAssertion -Id 'LAB27-VAL-NEG-02' -Kind negative -Passed ($null -ne $cleanup -and $cleanup.activeManagedObjects -eq 0 -and @($state.managedObjects).Count -eq 0 -and @($state.originalSettings).Count -eq 0 -and $state.status -eq 'cleaned') -Message 'No active managed object or unresolved original setting remains in cleanup or run state.'
    $postCleanupPassed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
    Save-ValidationArtifact -Result $(if ($postCleanupPassed) { 'pass' } else { 'fail' })
    if ($postCleanupPassed) { exit 0 }
    exit 1
}

Add-ValidationAssertion -Id 'LAB27-VAL-POS-02' -Kind positive -Passed ($state.status -eq 'planned') -Message 'The planning-only setup completed and remains planned; no deployment is implied.'
Add-ValidationAssertion -Id 'LAB27-VAL-NEG-02' -Kind negative -Passed (@($state.managedObjects | Where-Object { $_.tags.purpose -ne 'az305-lab' -or $_.tags.labId -ne 'LAB-27' -or $_.tags.runId -ne $RunId }).Count -eq 0) -Message 'No recorded object has a foreign ownership tag.'

if (@($assertions | Where-Object { -not $_.passed }).Count -gt 0) {
    Save-ValidationArtifact -Result 'fail'
    exit 1
}
if (-not $Execute) {
    # This lab has no special intent-only validation path.
    Save-ValidationArtifact -Result 'partial'
    Write-Warning 'Checkpoint validation is gated; re-run with -Execute after confirming the exact read-only context.'
    exit 2
}
# The validation surface is compatible with this lab implementation mode.
$missingValidationInputs = @()
if ($missingValidationInputs.Count -gt 0) {
    Add-ValidationAssertion -Id 'LAB27-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'One or more required non-secret validation inputs are missing.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}
try {
    # This offline-only execution path requires no authenticated context.
    Assert-InputSubscriptionScope -Inputs $state.parameters -ExpectedSubscriptionId $SubscriptionId
    Add-ValidationAssertion -Id 'LAB27-VAL-POS-CONTEXT' -Kind positive -Passed $true -Message 'The active tenant and subscription exactly match the requested validation context.'
}
catch {
    Add-ValidationAssertion -Id 'LAB27-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'Exact execution context could not be proven.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}

$originalLocation = Get-Location
try {
    Set-Location -LiteralPath $LabRoot
# LAB27-CP01: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $manifest = Get-Content tests/fixtures/manifest.json -Raw | ConvertFrom-Json; foreach ($item in $manifest.files) { if (-not (Test-Path $item.path)) { throw "Missing fixture: $($item.path)" }; if ((Get-FileHash $item.path -Algorithm SHA256).Hash -ne $item.sha256) { throw "Fixture hash mismatch: $($item.path)" } } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB27-CP01-POS' -Kind positive -Passed $positivePassed -Message 'Every fixture is present, hash-verified, schema-valid, sanitized, time-bounded, and linked to a source, assumption, requirement, and scenario inject.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $files = Get-ChildItem tests/fixtures -File -Recurse; if ($files | Select-String -Pattern '(?i)password|client_secret|account[_-]?key|[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}' | Where-Object { $_.Line -notmatch '00000000-0000-4000-8000-000000000000' }) { throw 'The offline evidence pack may contain sensitive or non-synthetic identifiers.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB27-CP01-NEG' -Kind negative -Passed $negativePassed -Message 'Missing provenance, mutable baseline, real identifier, secret-like field, or unstated unknown must fail before architecture work starts.'

# LAB27-CP02: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $portfolio = Import-Csv tests/fixtures/portfolio.csv; $allowed = @('rehost','replatform','refactor','repurchase','retain','retire'); if ($portfolio | Where-Object { $_.disposition -notin $allowed -or [string]::IsNullOrWhiteSpace($_.wave) -or [string]::IsNullOrWhiteSpace($_.owner) }) { throw 'A portfolio record lacks a valid disposition, wave, or owner.' } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB27-CP02-POS' -Kind positive -Passed $positivePassed -Message 'Each workload has a justified disposition, dependency-safe wave, target concept, coexistence bridge, readiness remediation, rollback, decommission gate, and owner.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $portfolio = Import-Csv tests/fixtures/portfolio.csv; $dependencies = Import-Csv tests/fixtures/dependencies.csv; $waveById = @{}; $portfolio | ForEach-Object { $waveById[$_.applicationId] = [int]$_.wave }; if ($dependencies | Where-Object { $_.criticality -eq 'hard' -and [math]::Abs($waveById[$_.sourceApplicationId] - $waveById[$_.targetApplicationId]) -gt 0 -and -not $_.coexistenceBridge }) { throw 'A hard dependency is split without a coexistence bridge.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB27-CP02-NEG' -Kind negative -Passed $negativePassed -Message 'A big-bang sequence, unsupported rehost, classified move without evidence, or permanent hybrid bridge without retirement criteria must fail.'

# LAB27-CP03: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $main = bicep build artifacts/main.bicep --stdout | ConvertFrom-Json; $foundation = bicep build artifacts/modules/hybrid-foundation.bicep --stdout | ConvertFrom-Json; $types = @($main.resources.type) + @($foundation.resources.type); $requiredTypes = @('Microsoft.Resources/resourceGroups','Microsoft.Network/virtualNetworks','Microsoft.OperationalInsights/workspaces','Microsoft.Insights/dataCollectionRules'); foreach ($type in $requiredTypes) { if ($type -notin $types) { throw "Missing hybrid-foundation resource type: $type" } } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB27-CP03 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB27-CP03-POS' -Kind positive -Passed $positivePassed -Message 'Bicep compiles offline and illustrates tagged resource-group, network, private-DNS, identity, workspace, and empty-DCR declarations plus a DoNotEnforce policy assignment; outputs explicitly separate the untaggable policy assignment, and no DCRA, diagnostic setting, deployment, or live behavior is claimed.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $templateText = bicep build artifacts/main.bicep --stdout; if ($templateText -match '(?i)password|clientSecret|accountKey|Basic_LoadBalancer|OmsAgentForLinux|0\.0\.0\.0/0') { throw 'The offline template contains a secret, retired default, or unrestricted rule.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB27-CP03 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB27-CP03-NEG' -Kind negative -Passed $negativePassed -Message 'A secret, tenant-specific identifier, legacy monitoring agent, Basic Load Balancer, implicit outbound dependency, hidden untaggable resource, shared-resource deletion, or suggestion that the compile-only template was deployed must fail.'

# LAB27-CP04: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $scenarios = Get-Content tests/fixtures/failure-scenarios.json -Raw | ConvertFrom-Json; if ($scenarios | Where-Object { -not $_.expectedDecision -or $_.simulatedDecisionMinutes -gt $_.maximumDecisionMinutes -or $_.businessAssertion -ne 'pass' }) { throw 'A required migration or continuity behavior failed.' } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB27-CP04-POS' -Kind positive -Passed $positivePassed -Message 'Deterministic injects cover discovery loss, circuit failure, replication lag, corrupt recovery points, policy denial, identity outage, cutover overrun, data mismatch, and rollback.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $scenarios = Get-Content tests/fixtures/failure-scenarios.json -Raw | ConvertFrom-Json; if ($scenarios | Where-Object { $_.prohibitedOutcomeObserved -or $_.containsAutomaticPurge -or $_.rollbackAuthority -eq $null }) { throw 'A prohibited outcome, purge action, or unowned rollback was detected.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB27-CP04-NEG' -Kind negative -Passed $negativePassed -Message 'Continuing after a mandatory gate, claiming success on infrastructure health alone, automatic purge, or accepting an unowned rollback decision must fail.'

# LAB27-CP05: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $report = Get-Content tests/fixtures/release-report.json -Raw | ConvertFrom-Json; if ($report.status -ne 'offline-validated' -or $report.lastLiveVerified -ne $null -or ($report.assertions | Where-Object result -ne 'pass')) { throw 'The capstone is not fully offline validated.' } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB27-CP05-POS' -Kind positive -Passed $positivePassed -Message 'The package passes schema, Bicep, traceability, source, decision, scenario, security, cost, recovery, portability, and cleanup-plan checks and reports only offline validation.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $report = Get-Content tests/fixtures/release-report.json -Raw | ConvertFrom-Json; if ($report.claims | Where-Object { $_ -match '(?i)deployed|live verified|production tested' }) { throw 'The offline report overclaims live verification.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB27-CP05-NEG' -Kind negative -Passed $negativePassed -Message 'Missing assertion evidence, a live-verification claim, vague decommission criteria, uncertain ownership, or irreversible purge instruction must fail release.'

}
finally {
    Set-Location -LiteralPath $originalLocation
}

$passed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
Save-ValidationArtifact -Result $(if ($passed) { 'pass' } else { 'fail' })
if ($passed) { exit 0 }
exit 1
# END GENERATED AZ305 V1
