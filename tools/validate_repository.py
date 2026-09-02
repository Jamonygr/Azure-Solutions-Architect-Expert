#!/usr/bin/env python3
"""Validate the complete AZ-305 repository without network or cloud access.

The release gate deliberately keeps cross-file policy here instead of weakening the
closed JSON Schemas.  It reports every issue it can discover in one run so a failed
build is actionable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable, Iterator
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
BEGIN = "BEGIN GENERATED AZ305 V1"
END = "END GENERATED AZ305 V1"
SCHEMA_VERSION = "1.0.0"

EXPECTED_LABS = [f"LAB-{index:02d}" for index in range(28)]
INSTRUCTIONAL_LABS = [f"LAB-{index:02d}" for index in range(1, 26)]
FOUNDATION_IDS = {
    "FD-TOOLS-01",
    "FD-CONTEXT-01",
    "FD-COST-01",
    "FD-SAFETY-01",
    "FD-CLEANUP-01",
}
EXPECTED_MODES = {
    "design-simulation": {"LAB-00", "LAB-14", "LAB-22", "LAB-27"},
    "reference-deployable": {
        "LAB-01", "LAB-02", "LAB-05", "LAB-08", "LAB-09", "LAB-10",
        "LAB-11", "LAB-12", "LAB-18", "LAB-20",
    },
    "safe-analogue": {
        "LAB-03", "LAB-04", "LAB-06", "LAB-07", "LAB-13", "LAB-15",
        "LAB-16", "LAB-17", "LAB-19", "LAB-21", "LAB-23", "LAB-24",
        "LAB-25", "LAB-26",
    },
}
EXPECTED_BICEP = {"LAB-18", "LAB-21", "LAB-26", "LAB-27"}
WAF_KEYS = {
    "reliability",
    "security",
    "costOptimization",
    "operationalExcellence",
    "performanceEfficiency",
}
ARCHITECTURE_FACT_KEYS = {"data", "scale", "latency", "availability", "rto", "rpo", "budget"}
BANNED_ARCHITECTURE_SCAFFOLDS = (
    "architecture evidence is synthetic or sanitized",
    "the design evaluates five independently testable capabilities",
    "latency targets are treated as workload requirements",
    "availability is evaluated across explicit failure domains",
    "recovery time is documented when the scenario owns continuity",
    "recovery point is documented when data protection is in scope",
    "the design may be overfit to the initial workload profile",
    "an operator could mistake offline evidence for live service proof",
    "scored against this scenario's mandatory fit",
    "fit is weaker for the stated mandatory requirements and operating model",
    "model failure domains, recovery dependencies, and degraded behavior before selection",
    "use least privilege, explicit trust boundaries, and evidence that excludes secrets",
    "re-score all eligible candidates, update the adr",
)
README_SECTIONS = [
    "Navigation",
    "Scenario and completion contract",
    "Objective-to-evidence map",
    "Business and quality requirements",
    "Architecture diagram and walkthrough",
    "Concept primer and candidate architectures",
    "Decision, ADR, and Well-Architected review",
    "Inputs, permissions, licensing, cost, and analogue",
    "Read-only preflight",
    "Five guided checkpoints",
    "Final validation and interpretation",
    "Material change request",
    "Architect job challenge",
    "Troubleshooting, cleanup, and residual verification",
    "Exam debrief, assessment, sources, and navigation",
    "Synchronized lifecycle-script appendix",
]
LIFECYCLE_SCRIPTS = ("Preflight.ps1", "Setup.ps1", "Validate.ps1", "Cleanup.ps1")
TEXT_SUFFIXES = {
    ".bicep", ".css", ".csv", ".html", ".ini", ".js", ".json", ".md",
    ".mjs", ".ps1", ".psd1", ".psm1", ".py", ".svg", ".txt", ".yaml", ".yml",
}
IGNORED_PARTS = {".git", ".state", ".site-docs", "site", "node_modules", "__pycache__", ".venv"}


@dataclass
class Report:
    checks: int = 0
    issues: list[str] = field(default_factory=list)

    def require(self, condition: bool, location: str, message: str) -> bool:
        self.checks += 1
        if not condition:
            self.issues.append(f"{location}: {message}")
        return condition

    def issue(self, location: str, message: str) -> None:
        self.checks += 1
        self.issues.append(f"{location}: {message}")


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return str(path)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def load_data(path: Path, report: Report | None = None) -> dict[str, Any] | None:
    try:
        data = yaml.safe_load(read_text(path))
    except (OSError, UnicodeError, yaml.YAMLError, json.JSONDecodeError) as exc:
        if report:
            report.issue(rel(path), f"cannot parse structured data: {exc}")
            return None
        raise
    if not isinstance(data, dict):
        if report:
            report.issue(rel(path), "top-level value must be an object")
            return None
        raise ValueError(f"Expected an object in {path}")
    return data


def official_objectives(blueprint: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for domain in blueprint.get("domains", []):
        for group in domain.get("groups", []):
            for objective in group.get("objectives", []):
                result[str(objective.get("id"))] = objective
    return result


def foundation_objectives(blueprint: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item.get("id")): item for item in blueprint.get("foundationObjectives", [])}


def schema_issues(instance: Any, schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    result = []
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.absolute_path)):
        pointer = "/" + "/".join(str(part) for part in error.absolute_path) if error.absolute_path else "/"
        result.append(f"{pointer}: {error.message}")
    return result


def validate_schema_document(path: Path, schema_path: Path, report: Report) -> dict[str, Any] | None:
    report.require(path.is_file(), rel(path), "required file is missing")
    report.require(schema_path.is_file(), rel(schema_path), "schema file is missing")
    if not path.is_file() or not schema_path.is_file():
        return None
    document = load_data(path, report)
    schema = load_data(schema_path, report)
    if document is None or schema is None:
        return document
    for issue in schema_issues(document, schema):
        report.issue(rel(path), f"schema {issue}")
    return document


def validate_schema_contracts(report: Report) -> None:
    schema_dir = ROOT / "schemas"
    schema_files = sorted(schema_dir.glob("*-schema.json"))
    report.require(len(schema_files) >= 13, "schemas", "expected the complete closed schema set")
    ids: set[str] = set()
    for path in schema_files:
        schema = load_data(path, report)
        if schema is None:
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:  # jsonschema exposes several schema-error subclasses
            report.issue(rel(path), f"is not a valid Draft 2020-12 schema: {exc}")
        schema_id = schema.get("$id")
        report.require(schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema", rel(path), "must declare JSON Schema Draft 2020-12")
        report.require(isinstance(schema_id, str) and schema_id.startswith("urn:az305:schema:") and schema_id.endswith(":" + SCHEMA_VERSION), rel(path), "must use a local versioned AZ-305 URN $id")
        report.require(schema_id not in ids, rel(path), f"duplicate schema $id {schema_id!r}")
        if isinstance(schema_id, str):
            ids.add(schema_id)
        report.require(schema.get("type") == "object", rel(path), "root schema must describe an object")
        report.require(schema.get("additionalProperties") is False, rel(path), "root schema must be closed")


def validate_source_models(report: Report) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]] | None:
    targets = (
        ("curriculum/blueprint.yml", "schemas/blueprint-schema.json"),
        ("curriculum/lab-catalog.yml", "schemas/lab-catalog-schema.json"),
        ("curriculum/lab-content.yml", "schemas/lab-content-schema.json"),
        ("curriculum/sources.yml", "schemas/source-registry-schema.json"),
        ("curriculum/commands.yml", "schemas/command-registry-schema.json"),
        ("curriculum/tool-versions.yml", "schemas/tool-versions-schema.json"),
    )
    values: list[dict[str, Any] | None] = []
    for document, schema in targets:
        values.append(validate_schema_document(ROOT / document, ROOT / schema, report))
    if any(value is None for value in values[:5]):
        return None
    blueprint, catalog, content, sources, commands = values[:5]
    assert blueprint is not None and catalog is not None and content is not None
    assert sources is not None and commands is not None
    required_baseline_urls = {
        "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305",
        "https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/",
        "https://learn.microsoft.com/en-us/training/paths/microsoft-azure-architect-design-prerequisites/",
        "https://learn.microsoft.com/en-us/training/paths/design-identity-governance-monitor-solutions/",
        "https://learn.microsoft.com/en-us/training/paths/design-data-storage-solutions/",
        "https://learn.microsoft.com/en-us/training/paths/design-business-continuity-solutions/",
        "https://learn.microsoft.com/en-us/training/paths/design-infranstructure-solutions/",
        "https://learn.microsoft.com/en-us/azure/architecture/patterns/",
        "https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/data-collection-rule-overview",
        "https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/retirement-faq",
        "https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-best-practices",
        "https://learn.microsoft.com/en-us/azure/frontdoor/classic-retirement-faq",
    }
    registered_urls = {str(item.get("url")) for item in sources.get("sources", [])}
    missing_baseline_urls = sorted(required_baseline_urls - registered_urls)
    report.require(
        not missing_baseline_urls,
        "curriculum/sources.yml",
        f"frozen baseline source URL(s) missing: {missing_baseline_urls}",
    )
    return blueprint, catalog, content, sources, commands


def validate_counts_and_mapping(
    blueprint: dict[str, Any], catalog: dict[str, Any], content: dict[str, Any], report: Report
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    official = official_objectives(blueprint)
    foundation = foundation_objectives(blueprint)
    labs = {str(item.get("id")): item for item in catalog.get("labs", [])}
    content_by_id = {f"LAB-{str(item.get('number', '')).zfill(2)}": item for item in content.get("labs", [])}

    report.require(len(official) == 49, "curriculum/blueprint.yml", f"expected 49 official objectives, found {len(official)}")
    report.require(set(foundation) == FOUNDATION_IDS, "curriculum/blueprint.yml", "foundation objective IDs must be the fixed five non-exam IDs")
    for objective_id, objective in foundation.items():
        report.require(objective.get("examObjective") is False, objective_id, "foundation objective must be explicitly non-exam")
        report.require(objective.get("primaryLab") == "LAB-00", objective_id, "foundation objective must be owned by LAB-00")

    report.require(list(labs) == EXPECTED_LABS, "curriculum/lab-catalog.yml", "labs must be ordered exactly LAB-00 through LAB-27")
    report.require(catalog.get("navigation", {}).get("sequence") == EXPECTED_LABS, "curriculum/lab-catalog.yml", "navigation sequence must be exactly LAB-00 through LAB-27")
    report.require(set(content_by_id) == set(EXPECTED_LABS), "curriculum/lab-content.yml", "authored content must contain each of the 28 labs exactly once")

    ownership: defaultdict[str, list[str]] = defaultdict(list)
    for lab_id in INSTRUCTIONAL_LABS:
        for objective_id in labs.get(lab_id, {}).get("primaryObjectiveIds", []):
            ownership[str(objective_id)].append(lab_id)
    report.require(set(ownership) == set(official), "curriculum/lab-catalog.yml", "instructional primary-objective union must equal the 49 official objectives")
    for objective_id in sorted(set(official) | set(ownership)):
        owners = ownership.get(objective_id, [])
        report.require(len(owners) == 1, objective_id, f"must have exactly one instructional primary lab; found {owners}")
        if objective_id in official and owners:
            report.require(official[objective_id].get("primaryLab") == owners[0], objective_id, "blueprint primaryLab disagrees with catalog ownership")
    report.require(set(labs.get("LAB-00", {}).get("primaryObjectiveIds", [])) == FOUNDATION_IDS, "LAB-00", "must own exactly the five foundation objectives")
    for lab_id in ("LAB-26", "LAB-27"):
        report.require(labs.get(lab_id, {}).get("primaryObjectiveIds") == [], lab_id, "capstones must reinforce, not own, official objectives")
        report.require(labs.get(lab_id, {}).get("reinforcesAllOfficialObjectives") is True, lab_id, "capstone must reinforce all official objectives")

    for mode, expected in EXPECTED_MODES.items():
        actual = {lab_id for lab_id, lab in labs.items() if lab.get("implementationMode") == mode}
        report.require(actual == expected, "curriculum/lab-catalog.yml", f"{mode} mapping differs: expected {sorted(expected)}, found {sorted(actual)}")
    report.require(labs.get("LAB-03", {}).get("track") == "azure-powershell", "LAB-03", "must use the azure-powershell track")
    report.require(labs.get("LAB-07", {}).get("track") == "azure-powershell", "LAB-07", "must use the azure-powershell track")
    bicep_labs = {lab_id for lab_id, lab in labs.items() if lab.get("supplementalBicep") is True}
    report.require(bicep_labs == EXPECTED_BICEP, "curriculum/lab-catalog.yml", f"Bicep lab set must be {sorted(EXPECTED_BICEP)}")

    for index, lab_id in enumerate(EXPECTED_LABS):
        lab = labs.get(lab_id, {})
        report.require(lab.get("number") == f"{index:02d}", lab_id, "number must agree with ID")
        report.require(lab.get("previousLabId") == (EXPECTED_LABS[index - 1] if index else None), lab_id, "previous navigation is incorrect")
        report.require(lab.get("nextLabId") == (EXPECTED_LABS[index + 1] if index < 27 else None), lab_id, "next navigation is incorrect")
        report.require(lab.get("status") == "offline-validated" and lab.get("lastLiveVerified") is None, lab_id, "must finish offline-validated with null live verification")
        authored = content_by_id.get(lab_id)
        if authored:
            report.require(str(authored.get("number", "")).zfill(2) == f"{index:02d}", lab_id, "authored content number differs from catalog")
            report.require(len(authored.get("checkpoints", [])) == 5, lab_id, "authored content must contain exactly five checkpoints")
            expected_requirements = {f"LAB{index:02d}-REQ-{cp:02d}" for cp in range(1, 6)}
            actual_requirements = {str(cp.get("requirement")) for cp in authored.get("checkpoints", [])}
            report.require(actual_requirements == expected_requirements, lab_id, "checkpoint requirement IDs must be the exact REQ-01 through REQ-05 set")
    return official, labs, content_by_id


def normalized_architecture_prose(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value)).strip().casefold()


def validate_architecture_specificity(
    labs: dict[str, dict[str, Any]], content_by_id: dict[str, dict[str, Any]], report: Report
) -> None:
    """Reject structurally valid but repeated or generic architecture filler."""
    prose_by_kind: defaultdict[str, list[tuple[str, str]]] = defaultdict(list)
    score_signatures: dict[tuple[tuple[int, ...], ...], str] = {}
    weights = {"C1": 30, "C2": 25, "C3": 20, "C4": 15, "C5": 10}
    for lab_id in EXPECTED_LABS:
        lab = labs.get(lab_id, {})
        content = content_by_id.get(lab_id, {})
        analysis = content.get("architectureAnalysis", {})
        report.require(isinstance(analysis, dict) and bool(analysis), lab_id, "authored architectureAnalysis is required")
        if not isinstance(analysis, dict):
            continue

        facts = analysis.get("facts", {})
        report.require(set(facts) == ARCHITECTURE_FACT_KEYS, lab_id, "analysis facts must cover exactly data, scale, latency, availability, RTO, RPO, and budget")
        for key in sorted(ARCHITECTURE_FACT_KEYS):
            value = normalized_architecture_prose(facts.get(key, ""))
            prose_by_kind[f"fact:{key}"].append((lab_id, value))

        candidates = analysis.get("candidateAnalyses", [])
        names = [str(item.get("name")) for item in candidates if isinstance(item, dict)]
        report.require(len(candidates) >= 4 and len(names) == len(set(names)), lab_id, "analysis needs at least four uniquely named candidates")
        report.require(set(content.get("candidates", [])).issubset(set(names)), lab_id, "analysis must include every scenario candidate")
        eligible = [item for item in candidates if item.get("eligible") is True and not item.get("disqualifiers")]
        disqualified = [item for item in candidates if item.get("eligible") is False and item.get("disqualifiers")]
        report.require(len(eligible) >= 3, lab_id, "analysis must retain at least three eligible candidates")
        report.require(bool(disqualified), lab_id, "analysis must document at least one specifically disqualified candidate")
        selected_name = str(content.get("selected"))
        by_name = {str(item.get("name")): item for item in candidates}
        selected = by_name.get(selected_name)
        report.require(selected is not None and selected.get("eligible") is True and not selected.get("disqualifiers"), lab_id, "authored selected candidate must be eligible in the analysis")
        eligible_totals: dict[str, float] = {}
        for item in candidates:
            candidate_name = str(item.get("name"))
            scores = item.get("scores", {})
            report.require(set(scores) == set(weights), f"{lab_id}/{candidate_name}", "analysis candidate must score C1 through C5 exactly")
            if set(scores) == set(weights) and all(type(value) is int for value in scores.values()):
                total = sum(weights[key] * scores[key] for key in weights) / 5
                if item.get("eligible") and not item.get("disqualifiers"):
                    eligible_totals[candidate_name] = total
            rationale = normalized_architecture_prose(item.get("rationale", ""))
            prose_by_kind["candidate rationale"].append((lab_id, rationale))
            rejected_reason = item.get("rejectedReason")
            if candidate_name == selected_name:
                report.require(rejected_reason is None, f"{lab_id}/{candidate_name}", "selected candidate must have a null rejectedReason")
            else:
                report.require(isinstance(rejected_reason, str) and len(rejected_reason.strip()) >= 30, f"{lab_id}/{candidate_name}", "every non-selected candidate needs a specific rejection reason")
                prose_by_kind["rejected reason"].append((lab_id, normalized_architecture_prose(rejected_reason)))
        if selected_name in eligible_totals:
            report.require(eligible_totals[selected_name] == max(eligible_totals.values()), lab_id, "authored selected candidate must have the highest eligible weighted total")

        if candidates and all(isinstance(item.get("scores"), dict) for item in candidates):
            signature = tuple(tuple(int(item["scores"].get(key, 0)) for key in weights) for item in candidates)
            prior = score_signatures.get(signature)
            report.require(prior is None, lab_id, f"complete decision score profile duplicates {prior}")
            score_signatures.setdefault(signature, lab_id)

        risks = analysis.get("risks", [])
        for item in risks:
            prose_by_kind["risk"].append((lab_id, normalized_architecture_prose(item.get("risk", ""))))
            prose_by_kind["mitigation"].append((lab_id, normalized_architecture_prose(item.get("mitigation", ""))))
        for key in sorted(WAF_KEYS):
            prose_by_kind[f"WAF:{key}"].append((lab_id, normalized_architecture_prose(analysis.get("waf", {}).get(key, ""))))

        revision = analysis.get("revisedDecision", {})
        revised_name = str(revision.get("selectedCandidate"))
        revised_candidate = by_name.get(revised_name)
        report.require(revised_candidate is not None and revised_candidate.get("eligible") is True and not revised_candidate.get("disqualifiers"), lab_id, "revised selection must name an eligible analyzed candidate")
        mandatory_id = str(revision.get("mandatoryRequirementId"))
        report.require(mandatory_id in str(revision.get("reason", "")), lab_id, "authored revised reason must cite its mandatory requirement ID")
        report.require(set(revision.get("waf", {})) == WAF_KEYS, lab_id, "revised decision must state all five WAF consequences")
        for key in sorted(WAF_KEYS):
            prose_by_kind[f"revised WAF:{key}"].append((lab_id, normalized_architecture_prose(revision.get("waf", {}).get(key, ""))))

        analogue = analysis.get("safeAnalogue")
        mode = lab.get("implementationMode")
        report.require(analogue is None if mode == "reference-deployable" else isinstance(analogue, str) and len(analogue.strip()) >= 40, lab_id, "analysis safe analogue does not match implementation mode")

        corpus = normalized_architecture_prose(analysis)
        for scaffold in BANNED_ARCHITECTURE_SCAFFOLDS:
            report.require(scaffold not in corpus, lab_id, f"generic architecture scaffold is prohibited: {scaffold!r}")

    for kind, entries in prose_by_kind.items():
        counts = Counter(value for _, value in entries if value)
        duplicates = sorted(value for value, count in counts.items() if count > 1)
        report.require(not duplicates, "curriculum/lab-content.yml", f"repeated exact {kind} prose detected across labs: {duplicates[:2]}")


def marker_wrapper(path: Path) -> tuple[str, str] | None:
    suffix = path.suffix.lower()
    if suffix in {".md", ".svg"}:
        return f"<!-- {BEGIN} -->", f"<!-- {END} -->"
    if suffix in {".ps1", ".yml", ".yaml"}:
        return f"# {BEGIN}", f"# {END}"
    if suffix == ".mmd":
        return f"%% {BEGIN}", f"%% {END}"
    if suffix == ".bicep":
        return f"// {BEGIN}", f"// {END}"
    return None


def extract_generated_body(text: str, path: Path | None = None) -> str:
    wrapper = marker_wrapper(path or Path("value.md"))
    if not wrapper:
        raise ValueError("unsupported generated file type")
    begin, end = wrapper
    if text.count(BEGIN) != 1 or text.count(END) != 1:
        raise ValueError("must contain exactly one begin marker and one end marker")
    start = text.find(begin)
    finish = text.find(end)
    if start < 0 or finish < 0 or finish <= start:
        raise ValueError("markers use the wrong wrapper or are out of order")
    body_start = start + len(begin)
    body = text[body_start:finish]
    if BEGIN in body or END in body:
        raise ValueError("nested generated markers are forbidden")
    return body.strip("\r\n")


def expected_generated_paths(lab: dict[str, Any]) -> list[Path]:
    folder = ROOT / "labs" / str(lab.get("folder", ""))
    track = str(lab.get("track", ""))
    paths = [
        folder / "lab.yml",
        folder / "design/requirements.yml",
        folder / "design/decision.yml",
        folder / "diagrams/architecture.mmd",
        folder / "diagrams/architecture.svg",
        folder / "README.md",
        folder / "solution/README.md",
        folder / "tests/README.md",
        folder / "tests/Contract.Tests.ps1",
    ]
    paths.extend(folder / "scripts" / track / name for name in LIFECYCLE_SCRIPTS)
    number = int(str(lab.get("number", "99")))
    if 1 <= number <= 25:
        paths.extend(
            [
                folder / "assessment/questions.yml",
                folder / "assessment/QUESTIONS.md",
                folder / "assessment/ANSWERS.md",
            ]
        )
    if lab.get("supplementalBicep"):
        paths.append(folder / "artifacts/main.bicep")
    return paths


def validate_markers_and_layout(labs: dict[str, dict[str, Any]], report: Report) -> None:
    expected_folders = {str(lab.get("folder")) for lab in labs.values()}
    actual_folders = {path.name for path in (ROOT / "labs").iterdir() if path.is_dir()} if (ROOT / "labs").is_dir() else set()
    report.require(actual_folders == expected_folders, "labs", f"lab folders differ from catalog; missing={sorted(expected_folders - actual_folders)}, extra={sorted(actual_folders - expected_folders)}")
    for lab_id, lab in labs.items():
        folder = ROOT / "labs" / str(lab.get("folder", ""))
        for path in expected_generated_paths(lab):
            if not report.require(path.is_file(), rel(path), "required generated artifact is missing"):
                continue
            try:
                extract_generated_body(read_text(path), path)
            except ValueError as exc:
                report.issue(rel(path), str(exc))
        for fixture in ("run.sample.json", "validation.sample.json", "cleanup.sample.json"):
            path = folder / "tests/fixtures" / fixture
            if not report.require(path.is_file(), rel(path), "required fixture is missing"):
                continue
            text = read_text(path)
            report.require(text.count(BEGIN) == 1 and text.count(END) == 1 and text.find(BEGIN) < text.find(END), rel(path), "JSON fixture markers must occur once and in order")
        tracks = {path.name for path in (folder / "scripts").iterdir() if path.is_dir()} if (folder / "scripts").is_dir() else set()
        report.require(tracks == {lab.get("track")}, lab_id, f"scripts must contain only the assigned track folder; found {sorted(tracks)}")
        if lab_id in EXPECTED_BICEP:
            report.require((folder / "artifacts/parameters.example.json").is_file(), lab_id, "Bicep lab is missing parameters.example.json")
        else:
            report.require(not (folder / "artifacts/main.bicep").exists(), lab_id, "Bicep is present outside the fixed four-lab set")


def validate_generated_schemas(labs: dict[str, dict[str, Any]], report: Report) -> None:
    schemas = {
        "lab": load_data(ROOT / "schemas/lab-schema.json", report),
        "requirements": load_data(ROOT / "schemas/requirements-schema.json", report),
        "decision": load_data(ROOT / "schemas/decision-schema.json", report),
        "questions": load_data(ROOT / "schemas/questions-schema.json", report),
        "run": load_data(ROOT / "schemas/run-schema.json", report),
        "validation": load_data(ROOT / "schemas/validation-schema.json", report),
        "cleanup": load_data(ROOT / "schemas/cleanup-schema.json", report),
    }
    if any(value is None for value in schemas.values()):
        return
    for lab_id, lab in labs.items():
        folder = ROOT / "labs" / str(lab.get("folder", ""))
        documents = [
            (folder / "lab.yml", schemas["lab"]),
            (folder / "design/requirements.yml", schemas["requirements"]),
            (folder / "design/decision.yml", schemas["decision"]),
            (folder / "tests/fixtures/run.sample.json", schemas["run"]),
            (folder / "tests/fixtures/validation.sample.json", schemas["validation"]),
            (folder / "tests/fixtures/cleanup.sample.json", schemas["cleanup"]),
        ]
        if lab_id in INSTRUCTIONAL_LABS:
            documents.append((folder / "assessment/questions.yml", schemas["questions"]))
        for path, schema in documents:
            if not path.is_file() or schema is None:
                continue
            instance = load_data(path, report)
            if instance is None:
                continue
            for issue in schema_issues(instance, schema):
                report.issue(rel(path), f"schema {issue}")


def validate_decision(decision: dict[str, Any], requirements: dict[str, Any], lab: dict[str, Any], report: Report) -> None:
    lab_id = str(lab.get("id"))
    criteria = decision.get("criteria", [])
    weights = {str(item.get("id")): item.get("weight") for item in criteria}
    report.require(len(weights) == len(criteria), lab_id, "decision criteria IDs must be unique")
    report.require(sum(value for value in weights.values() if isinstance(value, int)) == 100, lab_id, "decision criterion weights must total 100")
    candidates = decision.get("candidates", [])
    names = [str(item.get("name")) for item in candidates]
    report.require(len(names) == len(set(names)) and len(names) >= 4, lab_id, "decision needs at least four uniquely named candidates")
    by_name = {str(item.get("name")): item for item in candidates}
    for candidate in candidates:
        name = str(candidate.get("name"))
        scores = candidate.get("scores", {})
        report.require(set(scores) == set(weights), f"{lab_id}/{name}", "candidate must score every and only declared criterion")
        score_values = list(scores.values()) if isinstance(scores, dict) else []
        report.require(all(type(value) is int and 1 <= value <= 5 for value in score_values), f"{lab_id}/{name}", "decision scores must be integers from 1 through 5")
        calculated = sum(weights[key] * scores[key] for key in weights if key in scores and isinstance(weights[key], int) and isinstance(scores[key], int)) / 5
        report.require(math.isclose(float(candidate.get("weightedTotal", -1)), calculated, abs_tol=1e-9), f"{lab_id}/{name}", f"weighted total must be sum(weight × score) / 5 = {calculated:g}")
        if candidate.get("disqualifiers"):
            report.require(candidate.get("eligible") is False, f"{lab_id}/{name}", "a disqualified candidate must be ineligible")
    viable = [item for item in candidates if item.get("eligible") is True and not item.get("disqualifiers")]
    disqualified = [item for item in candidates if item.get("eligible") is False and item.get("disqualifiers")]
    report.require(len(viable) >= 3, lab_id, "decision must retain at least three eligible candidates")
    report.require(bool(disqualified), lab_id, "decision must include at least one specifically disqualified candidate")
    selected_name = str(decision.get("selectedCandidate"))
    selected = by_name.get(selected_name)
    report.require(selected is not None, lab_id, "selected candidate is absent from candidate matrix")
    if selected:
        report.require(selected.get("eligible") is True and not selected.get("disqualifiers"), lab_id, "selected candidate must be eligible and free of disqualifiers")
        viable_scores = [float(item.get("weightedTotal", -1)) for item in candidates if item.get("eligible") and not item.get("disqualifiers")]
        report.require(not viable_scores or float(selected.get("weightedTotal", -1)) == max(viable_scores), lab_id, "initial selection must be the highest-scoring eligible candidate")
    rejected = {str(item.get("candidate")) for item in decision.get("rejectedAlternatives", [])}
    report.require(rejected == set(names) - {selected_name}, lab_id, "rejected alternatives must name every non-selected candidate exactly once")
    report.require(set(decision.get("waf", {})) == WAF_KEYS, lab_id, "decision must address exactly all five WAF pillars")
    mode = lab.get("implementationMode")
    analogue = decision.get("safeAnalogue")
    report.require((isinstance(analogue, str) and len(analogue.strip()) >= 20) if mode != "reference-deployable" else analogue is None, lab_id, "safe analogue must be substantive for simulation/analogue modes and null for reference-deployable mode")
    report.require(decision.get("implementationMode") == mode, lab_id, "decision implementation mode differs from catalog")
    number = str(lab.get("number"))
    report.require(decision.get("adr", {}).get("id") == f"ADR-LAB{number}-001", lab_id, "ADR ID is not canonical")

    all_requirements = requirements.get("functionalRequirements", []) + requirements.get("nonfunctionalRequirements", [])
    requirements_by_id = {str(item.get("id")): item for item in all_requirements}
    revision = decision.get("revisedDecision", {})
    mandatory_id = str(revision.get("mandatoryRequirementId"))
    revised_candidate = by_name.get(str(revision.get("selectedCandidate")))
    report.require(revised_candidate is not None and revised_candidate.get("eligible") is True and not revised_candidate.get("disqualifiers"), lab_id, "revised decision must select an eligible analyzed candidate")
    report.require(mandatory_id in requirements_by_id and requirements_by_id.get(mandatory_id, {}).get("mandatory") is True, lab_id, "revised decision must cite an existing mandatory requirement")
    report.require(mandatory_id in str(revision.get("reason", "")), lab_id, "selection override reason must explicitly cite the mandatory requirement ID")
    report.require(revision.get("changeRequestId") == requirements.get("changeRequest", {}).get("id"), lab_id, "revised decision and material change request IDs differ")
    report.require(set(revision.get("waf", {})) == WAF_KEYS, lab_id, "revised decision must document all five WAF consequences")


def validate_traceability_and_labs(
    official: dict[str, dict[str, Any]], labs: dict[str, dict[str, Any]], sources: dict[str, Any], report: Report
) -> None:
    registered_urls = {str(item.get("url")) for item in sources.get("sources", [])}
    all_official = set(official)
    for lab_id, catalog_lab in labs.items():
        folder = ROOT / "labs" / str(catalog_lab.get("folder", ""))
        metadata = load_data(folder / "lab.yml", report) if (folder / "lab.yml").is_file() else None
        requirements = load_data(folder / "design/requirements.yml", report) if (folder / "design/requirements.yml").is_file() else None
        decision = load_data(folder / "design/decision.yml", report) if (folder / "design/decision.yml").is_file() else None
        if metadata is None or requirements is None or decision is None:
            continue
        report.require(metadata.get("id") == lab_id and metadata.get("slug") == catalog_lab.get("folder"), lab_id, "generated metadata identity differs from catalog")
        report.require(metadata.get("track") == catalog_lab.get("track"), lab_id, "generated track differs from catalog")
        report.require(metadata.get("implementationMode") == catalog_lab.get("implementationMode"), lab_id, "generated implementation mode differs from catalog")
        report.require(metadata.get("status") == "offline-validated" and metadata.get("lastLiveVerified") is None, lab_id, "generated lab must be offline-validated with null live verification")
        if lab_id == "LAB-00":
            expected_primary, expected_reinforced = FOUNDATION_IDS, set()
        elif lab_id in {"LAB-26", "LAB-27"}:
            expected_primary, expected_reinforced = set(), all_official
        else:
            expected_primary, expected_reinforced = set(catalog_lab.get("primaryObjectiveIds", [])), set()
        report.require(set(metadata.get("objectives", {}).get("primary", [])) == expected_primary, lab_id, "metadata primary objectives violate ownership")
        report.require(set(metadata.get("objectives", {}).get("reinforced", [])) == expected_reinforced, lab_id, "metadata reinforced objectives are incomplete")
        source_urls = set(metadata.get("sourceUrls", []))
        report.require(bool(source_urls) and source_urls <= registered_urls, lab_id, "lab source URLs must resolve through the frozen source registry")

        requirement_items = requirements.get("functionalRequirements", []) + requirements.get("nonfunctionalRequirements", [])
        req_map = {str(item.get("id")): item for item in requirement_items}
        checkpoints = metadata.get("checkpoints", [])
        cp_map = {str(item.get("id")): item for item in checkpoints}
        trace_rows = decision.get("traceability", [])
        trace = {(str(row.get("objectiveId")), str(row.get("requirementId")), str(row.get("checkpointId"))) for row in trace_rows}
        report.require(len(checkpoints) == 5 and len(cp_map) == 5, lab_id, "metadata must contain five uniquely identified checkpoints")
        report.require(len(req_map) == 5, lab_id, "requirements document must contain five uniquely identified requirements")
        report.require(len(trace) == len(trace_rows), lab_id, "decision trace rows must be unique")
        allowed_objectives = expected_primary | expected_reinforced
        for cp_id, checkpoint in cp_map.items():
            requirement_ids = set(checkpoint.get("requirementIds", []))
            objective_ids = set(checkpoint.get("objectiveIds", []))
            report.require(len(requirement_ids) == 1 and requirement_ids <= set(req_map), f"{lab_id}/{cp_id}", "checkpoint must map to exactly one existing requirement")
            expected_objective_count = len(objective_ids) == 1 if lab_id not in {"LAB-26", "LAB-27"} else len(objective_ids) >= 1
            report.require(expected_objective_count and objective_ids <= allowed_objectives, f"{lab_id}/{cp_id}", "checkpoint objective mapping is empty, outside the lab, or non-singular for a non-capstone")
            if requirement_ids and objective_ids:
                requirement_id = next(iter(requirement_ids))
                req = req_map[requirement_id]
                for objective_id in objective_ids:
                    row = (objective_id, requirement_id, cp_id)
                    report.require(row in trace, f"{lab_id}/{cp_id}", f"objective → requirement → checkpoint row is missing for {objective_id}")
                    report.require(objective_id in req.get("objectiveIds", []), f"{lab_id}/{cp_id}", f"requirement omits checkpoint objective {objective_id}")
        validate_decision(decision, requirements, catalog_lab, report)

        if lab_id in INSTRUCTIONAL_LABS:
            question_path = folder / "assessment/questions.yml"
            bank = load_data(question_path, report) if question_path.is_file() else None
            if bank:
                report.require(len(bank.get("questions", [])) == 50, lab_id, "instructional bank must contain exactly 50 questions")
                unregistered_question_sources: set[str] = set()
                for question in bank.get("questions", []):
                    qid = str(question.get("id"))
                    objective_id = str(question.get("objectiveId"))
                    cp_id = str(question.get("checkpointId"))
                    cp = cp_map.get(cp_id, {})
                    requirement_ids = cp.get("requirementIds", [])
                    expected_row = (objective_id, str(requirement_ids[0]), cp_id) if len(requirement_ids) == 1 else None
                    report.require(objective_id in expected_primary, qid, "question must map to one primary objective of its instructional lab")
                    report.require(expected_row in trace if expected_row else False, qid, "question mapping does not complete the decision trace chain")
                    if question.get("source") not in registered_urls:
                        unregistered_question_sources.add(str(question.get("source")))
                report.require(not unregistered_question_sources, lab_id, f"question source URL(s) absent from frozen registry: {sorted(unregistered_question_sources)}")
        else:
            report.require(not (folder / "assessment/questions.yml").exists(), lab_id, "non-instructional lab must not have a scored bank")


def extract_commands(text: str) -> list[str]:
    """Extract external Azure/Graph command surfaces from a command snippet."""
    commands: list[str] = []
    for raw_line in text.replace("`\n", " ").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        cli = re.search(r"(?<![A-Za-z0-9_.-])(azcopy|az)(?:\.cmd|\.exe)?\b(?!\.)(.+)?", line, re.IGNORECASE)
        if cli:
            tail = (cli.group(2) or "").strip()
            commands.append((cli.group(1).lower() + (" " + tail if tail else "")).strip())
        if re.search(r"(?<![A-Za-z0-9_-])bicep\s+build\b", line, re.IGNORECASE):
            commands.append("bicep build")
        commands.extend(
            match.group(0)
            for match in re.finditer(
                r"\b(?:Connect|Disconnect|Get|New|Set|Remove|Update|Test|Invoke|Start|Stop|Enable|Disable)-(?:Az|Mg)[A-Za-z0-9.]*\b",
                line,
                re.IGNORECASE,
            )
        )
    return commands


def command_allowed(command: str, track: str, registry: dict[str, Any]) -> bool:
    definition = registry.get("tracks", {}).get(track, {})
    normalized = " ".join(command.split())
    folded = normalized.casefold()
    for exact in definition.get("allowedCommands", []):
        expected = " ".join(str(exact).split()).casefold()
        if folded == expected or folded.startswith(expected + " "):
            return True
    for prefix in definition.get("allowedPrefixes", []):
        expected = " ".join(str(prefix).split()).casefold()
        if folded == expected or folded.startswith(expected + " ") or ("-" in expected and folded.startswith(expected)):
            return True
    return False


def validate_lane_commands(
    labs: dict[str, dict[str, Any]], content_by_id: dict[str, dict[str, Any]], registry: dict[str, Any], report: Report
) -> None:
    rules = registry.get("rules", {})
    report.require(rules.get("graphApiVersion") == "v1.0" and rules.get("betaModulesAllowed") is False, "curriculum/commands.yml", "only Microsoft Graph v1.0 commands are permitted")
    for lab_id, lab in labs.items():
        track = str(lab.get("track"))
        content = content_by_id.get(lab_id, {})
        snippets: list[tuple[str, str]] = []
        for checkpoint in content.get("checkpoints", []):
            snippets.extend((key, str(checkpoint.get(key, ""))) for key in ("command", "positiveCommand", "negativeCommand"))
        for field_name, snippet in snippets:
            if field_name != "negativeCommand":
                report.require("graph.microsoft.com/beta" not in snippet.casefold() and "microsoft.graph.beta" not in snippet.casefold(), lab_id, "Beta Graph commands or modules are forbidden")
            commands = extract_commands(snippet)
            for command in commands:
                folded = command.casefold()
                if track == "azure-cli":
                    report.require(folded.startswith("az ") or folded.startswith("azcopy ") or folded == "bicep build", lab_id, f"lane impurity: {command}")
                elif track == "azure-powershell":
                    report.require(not folded.startswith("az ") and not folded.startswith("azcopy "), lab_id, f"lane impurity: {command}")
                report.require(command_allowed(command, track, registry), lab_id, f"command is not covered by the {track} registry: {command}")

        script_root = ROOT / "labs" / str(lab.get("folder", "")) / "scripts" / track
        for path in (script_root.glob("*.ps1") if script_root.is_dir() else []):
            text = read_text(path)
            beta_use = re.search(r"(?im)^\s*(?:Import-Module|Connect-MgGraph|Invoke-MgGraphRequest)\b[^\r\n]*(?:Microsoft\.Graph\.Beta|/beta(?:/|\b))", text)
            report.require(beta_use is None, rel(path), "Beta Graph execution surface is forbidden")
            report.require(not re.search(r"(?im)^\s*(?:\.|Import-Module)\s+.*(?:\.\.[/\\]){2}|\b(?:curriculum|tools)[/\\]", text), rel(path), "portable lifecycle script imports repository-level helpers")
        setup = script_root / "Setup.ps1"
        if setup.is_file():
            text = read_text(setup)
            tokens = ["SubscriptionId", "TenantId", "RunId", "Location", "SecondaryLocation", "Execute", "AcknowledgeCost", "AcknowledgeTenantChange"]
            for token in tokens:
                report.require(f"${token}" in text, rel(setup), f"missing lifecycle parameter {token}")
            for fallback in ("AZ305_SUBSCRIPTION_ID", "AZ305_TENANT_ID", "AZ305_RUN_ID", "AZ305_LOCATION", "AZ305_SECONDARY_LOCATION"):
                report.require(fallback in text, rel(setup), f"missing environment fallback {fallback}")
            first_checkpoint = re.search(r"(?m)^\s*#\s*\d{2}-CP01:", text)
            state_write = text.find("Save-RunState -State $state")
            report.require(first_checkpoint is not None and 0 <= state_write < first_checkpoint.start(), rel(setup), "run.json state must be persisted before the first potential mutation")
        cleanup = script_root / "Cleanup.ps1"
        if cleanup.is_file():
            text = read_text(cleanup)
            for ownership in ("purpose", "labId", "runId", "expiresOn"):
                report.require(ownership in text, rel(cleanup), f"cleanup omits ownership proof {ownership}")
            report.require("[array]::Reverse" in text, rel(cleanup), "cleanup must reverse dependency order")
            purge_action = re.search(r"(?im)^\s*(?:Remove|Clear|Undo|az\s+\S+\s+purge)\S*.*\bpurge\b", text)
            report.require(purge_action is None, rel(cleanup), "cleanup must never automate purge")


def extract_appendix_script(readme: str, name: str) -> str | None:
    match = re.search(
        rf"(?ms)^### {re.escape(name)}\s*$\s*```powershell\s*\n(.*?)\n```",
        readme,
    )
    return match.group(1).rstrip() if match else None


def validate_readmes_and_sync(labs: dict[str, dict[str, Any]], report: Report) -> None:
    for lab_id, lab in labs.items():
        folder = ROOT / "labs" / str(lab.get("folder", ""))
        readme_path = folder / "README.md"
        if not readme_path.is_file():
            continue
        text = read_text(readme_path)
        headings = re.findall(r"(?m)^## ([0-9]+)\. (.+?)\s*$", text)
        expected = [(str(index), title) for index, title in enumerate(README_SECTIONS, 1)]
        report.require(headings == expected, rel(readme_path), "README must use the exact 16-section order")
        checkpoints = re.findall(r"(?m)^### Checkpoint ([1-5]):", text)
        report.require(checkpoints == ["1", "2", "3", "4", "5"], rel(readme_path), "README must expose exactly five ordered checkpoints")
        for index in range(1, 6):
            section_match = re.search(rf"(?ms)^### Checkpoint {index}:.*?(?=^### Checkpoint {index + 1}:|^## 11\.)", text)
            section = section_match.group(0) if section_match else ""
            for required_phrase in ("**Trace:**", "Expected evidence:", "Positive assertion:", "Negative assertion:", "Failure and retry:", "Cleanup dependency:", "WAF consequence:"):
                report.require(required_phrase in section, f"{lab_id}/checkpoint-{index}", f"missing {required_phrase}")
        for name in LIFECYCLE_SCRIPTS:
            script_path = folder / "scripts" / str(lab.get("track")) / name
            if not script_path.is_file():
                continue
            appendix = extract_appendix_script(text, name)
            report.require(appendix is not None, rel(readme_path), f"appendix does not contain {name}")
            try:
                script_body = extract_generated_body(read_text(script_path), script_path).rstrip()
            except ValueError:
                continue
            if appendix is not None:
                report.require(appendix.replace("\r\n", "\n") == script_body.replace("\r\n", "\n"), rel(readme_path), f"embedded {name} differs from the portable script")


def validate_lifecycle_contracts(labs: dict[str, dict[str, Any]], report: Report) -> None:
    parameters = (
        "SubscriptionId", "TenantId", "RunId", "Location", "SecondaryLocation",
        "Execute", "AcknowledgeCost", "AcknowledgeTenantChange",
    )
    fallbacks = (
        "AZ305_SUBSCRIPTION_ID", "AZ305_TENANT_ID", "AZ305_RUN_ID",
        "AZ305_LOCATION", "AZ305_SECONDARY_LOCATION",
    )
    shim_names = (
        "function global:az", "function global:Get-AzContext",
        "function global:Invoke-AzRestMethod", "function global:Connect-MgGraph",
        "function global:Invoke-MgGraphRequest", "function global:azcopy",
        "function global:Start-AzDataMigration",
    )
    for lab_id, lab in labs.items():
        folder = ROOT / "labs" / str(lab.get("folder", ""))
        script_root = folder / "scripts" / str(lab.get("track", ""))
        for name in LIFECYCLE_SCRIPTS:
            path = script_root / name
            if not path.is_file():
                continue
            text = read_text(path)
            for parameter in parameters:
                report.require(f"${parameter}" in text, rel(path), f"missing public lifecycle parameter {parameter}")
            for fallback in fallbacks:
                report.require(fallback in text, rel(path), f"missing lifecycle environment fallback {fallback}")
            for code in (0, 1, 2):
                report.require(re.search(rf"(?i)\bexit\s+{code}\b", text) is not None, rel(path), f"exit code {code} is not represented")
        validate_path = script_root / "Validate.ps1"
        if validate_path.is_file():
            text = read_text(validate_path)
            report.require("ValidateSet('Deployment', 'PostCleanup')" in text, rel(validate_path), "validation modes must be exactly Deployment and PostCleanup")
            report.require("-Kind positive" in text and "-Kind negative" in text, rel(validate_path), "positive and negative validation assertions must remain independent")
        tests_path = folder / "tests/Contract.Tests.ps1"
        if tests_path.is_file():
            text = read_text(tests_path)
            case_count = len(re.findall(r"(?m)^\s*It\s+['\"]", text))
            report.require(case_count >= 8, rel(tests_path), f"each lab needs at least eight Pester safety cases; found {case_count}")
            for shim in shim_names:
                report.require(shim in text, rel(tests_path), f"throwing cloud/migration shim is missing: {shim}")


def validate_workflows(report: Report) -> None:
    workflow_dir = ROOT / ".github/workflows"
    workflows = sorted(workflow_dir.glob("*.yml")) + sorted(workflow_dir.glob("*.yaml")) if workflow_dir.is_dir() else []
    report.require(bool(workflows), ".github/workflows", "at least one CI workflow is required")
    for path in workflows:
        text = read_text(path)
        report.require("pull_request_target" not in text, rel(path), "privileged pull_request_target is forbidden")
        for line_number, line in enumerate(text.splitlines(), 1):
            match = re.search(r"\buses:\s*([^\s#]+)", line)
            if not match:
                continue
            reference = match.group(1)
            if reference.startswith("./"):
                continue
            report.require(re.search(r"@[0-9a-fA-F]{40}$", reference) is not None, f"{rel(path)}:{line_number}", f"action must be pinned to a full commit SHA: {reference}")
    pages = workflow_dir / "pages.yml"
    report.require(pages.is_file(), rel(pages), "Pages workflow is missing")
    if pages.is_file():
        text = read_text(pages)
        report.require("AZ305_ENABLE_PAGES" in text and "== 'true'" in text, rel(pages), "deployment must be disabled unless AZ305_ENABLE_PAGES is explicitly true")
        gate_position = text.find("Invoke-OfflineReleaseGate.ps1")
        deploy_position = text.find("actions/deploy-pages")
        report.require(0 <= gate_position < deploy_position, rel(pages), "complete quality gate must precede Pages deployment")


def validate_assessment_totals(labs: dict[str, dict[str, Any]], report: Report) -> None:
    bank_count = 0
    question_count = 0
    for lab_id, lab in labs.items():
        path = ROOT / "labs" / str(lab.get("folder", "")) / "assessment/questions.yml"
        if lab_id in INSTRUCTIONAL_LABS and path.is_file():
            bank = load_data(path, report)
            if bank:
                bank_count += 1
                question_count += len(bank.get("questions", []))
        elif path.exists():
            report.issue(rel(path), "a scored bank is allowed only for LAB-01 through LAB-25")
    report.require(bank_count == 25, "labs/*/assessment/questions.yml", f"expected 25 banks, found {bank_count}")
    report.require(question_count == 1250, "labs/*/assessment/questions.yml", f"expected 1,250 questions, found {question_count}")


def validate_diagrams(labs: dict[str, dict[str, Any]], report: Report) -> None:
    for lab_id, lab in labs.items():
        folder = ROOT / "labs" / str(lab.get("folder", "")) / "diagrams"
        source_path = folder / "architecture.mmd"
        svg_path = folder / "architecture.svg"
        if not source_path.is_file() or not svg_path.is_file():
            continue
        source = read_text(source_path)
        svg = read_text(svg_path)
        expected_hash = hashlib.sha256(source.encode("utf-8")).hexdigest()
        report.require(f"source-sha256:{expected_hash}" in svg, lab_id, "SVG source hash does not match Mermaid source")
        for signal in ('role="img"', "aria-labelledby=", "<title", "<desc"):
            report.require(signal in svg, rel(svg_path), f"accessible SVG signal is missing: {signal}")
        report.require("<script" not in svg.casefold(), rel(svg_path), "SVG must not execute script")
        report.require(not re.search(r"(?:href|src)=[\"']https?://", svg, re.IGNORECASE), rel(svg_path), "SVG must not load an external active asset")


def validate_bicep_files(labs: dict[str, dict[str, Any]], report: Report) -> None:
    for lab_id in EXPECTED_BICEP:
        lab = labs.get(lab_id, {})
        folder = ROOT / "labs" / str(lab.get("folder", "")) / "artifacts"
        bicep = folder / "main.bicep"
        parameters = folder / "parameters.example.json"
        report.require(bicep.is_file(), lab_id, "required self-contained artifacts/main.bicep is missing")
        report.require(parameters.is_file(), lab_id, "required parameters.example.json is missing")
        if parameters.is_file():
            document = load_data(parameters, report)
            if document:
                report.require(document.get("contentVersion") == "1.0.0.0" and isinstance(document.get("parameters"), dict), rel(parameters), "invalid ARM parameters example")
        if bicep.is_file():
            text = read_text(bicep)
            report.require("../" not in text and "..\\" not in text, rel(bicep), "Bicep must be self-contained")
            report.require("purpose:" in text and "labId:" in text and "runId:" in text and "expiresOn:" in text, rel(bicep), "Bicep must declare the complete ownership tag contract")


def iter_repository_files() -> Iterator[Path]:
    git = shutil.which("git")
    if git and (ROOT / ".git").exists():
        result = subprocess.run(
            [git, "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
            cwd=ROOT,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )
        if result.returncode == 0:
            for raw in result.stdout.split(b"\0"):
                if raw:
                    path = ROOT / os.fsdecode(raw)
                    if path.is_file() and not any(part in IGNORED_PARTS for part in path.parts):
                        yield path
            return
    for path in ROOT.rglob("*"):
        if path.is_file() and not any(part in IGNORED_PARTS for part in path.parts):
            yield path


def validate_repository_hygiene(report: Report) -> None:
    legacy_tokens = ("AZ-" + "104", "az" + "104", "Azure Administrator" + " Associate", "AZ" + "104_")
    filler_tokens = ("TO" + "DO", "FIX" + "ME", "T" + "BD", "TK" + "TK", "lorem " + "ipsum", "place" + "holder")
    forbidden_extensions = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tiff"}
    guid_pattern = re.compile(r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")
    secret_patterns = [
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"\bAccountKey=[A-Za-z0-9+/=]{20,}"),
        re.compile(r"\b(?:eyJ[A-Za-z0-9_-]{10,}\.){2}[A-Za-z0-9_-]{8,}"),
        re.compile(r"(?i)\b(?:client[_-]?secret|password|access[_-]?token)\s*[:=]\s*[\"'][^\"']{8,}[\"']"),
    ]
    seen: set[Path] = set()
    for path in iter_repository_files():
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        relative = rel(path)
        lower_name = relative.casefold()
        report.require(path.suffix.casefold() not in forbidden_extensions, relative, "raster/screenshot-like assets are excluded from this release")
        for token in legacy_tokens:
            report.require(token.casefold() not in lower_name, relative, "filename contains a legacy reference-exam identifier")
        if path.suffix.casefold() not in TEXT_SUFFIXES and path.name not in {"Dockerfile", "LICENSE", ".gitignore", ".gitattributes", ".editorconfig", ".dockerignore"}:
            continue
        try:
            text = read_text(path)
        except (UnicodeError, OSError):
            continue
        report.require("\ufffd" not in text, relative, "contains a Unicode replacement character")
        report.require(
            not any(ord(character) < 32 and character not in "\r\n\t" for character in text),
            relative,
            "contains an unexpected control character",
        )
        folded = text.casefold()
        for token in legacy_tokens:
            report.require(token.casefold() not in folded, relative, "contains a legacy reference-exam identifier or environment variable")
        for token in filler_tokens:
            report.require(not re.search(rf"(?i)\b{re.escape(token)}\b", text), relative, f"contains unfinished filler token {token}")
        for pattern in secret_patterns:
            report.require(pattern.search(text) is None, relative, "contains credential-like material")
        for match in guid_pattern.finditer(text):
            guid = match.group(0).casefold()
            context = text[max(0, match.start() - 100):match.end() + 100].casefold()
            synthetic = bool(re.fullmatch(
                r"00000000-0000-(?:0000-0000-0000000003[0-9]{2}|4000-8000-(?:0000000003[0-9]{2}|00000000999[89]))",
                guid,
            )) or guid == "00000000-0000-4000-8000-000000000000"
            platform_definition = "roledefinition" in context or "policydefinition" in context or "microsoft.authorization/roledefinitions" in context
            report.require(synthetic or platform_definition, relative, f"contains a non-reserved, non-platform GUID: {guid}")
        verbs = "(?:" + "|".join(("op" + "en", "bro" + "wse", "navi" + "gate", "cl" + "ick", "sel" + "ect")) + ")"
        destination = "(?:azure\\s+" + "por" + "tal|" + "por" + "tal)"
        procedure = re.search(rf"(?i)\b{verbs}\b[^\r\n]{{0,80}}\b{destination}\b", text)
        report.require(procedure is None, relative, "contains an interactive Portal procedure")


def markdown_anchors(text: str) -> set[str]:
    anchors = set(re.findall(r"(?i)<a\s+(?:[^>]*?\s)?id=[\"']([^\"']+)[\"']", text))
    for heading in re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", text):
        value = re.sub(r"[^a-z0-9 _-]", "", re.sub(r"`([^`]*)`", r"\1", heading).casefold())
        anchors.add(re.sub(r"[ _]+", "-", value).strip("-"))
    return anchors


def validate_internal_links(report: Report) -> None:
    markdown_files = [path for path in iter_repository_files() if path.suffix.casefold() == ".md"]
    anchor_cache: dict[Path, set[str]] = {}
    link_pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)|!\[[^\]]*\]\(([^)]+)\)")
    for path in markdown_files:
        text = read_text(path)
        for match in link_pattern.finditer(text):
            raw = (match.group(1) or match.group(2) or "").strip()
            if raw.startswith("<") and raw.endswith(">"):
                raw = raw[1:-1]
            raw = raw.split(" ", 1)[0]
            parts = urlsplit(raw)
            if parts.scheme in {"http", "https", "mailto", "data"} or raw.startswith("//"):
                continue
            target_text = unquote(parts.path)
            target = path if not target_text else (path.parent / target_text)
            if target.is_dir():
                target = target / "README.md"
            report.require(target.is_file(), rel(path), f"broken local link target {raw!r}")
            if target.is_file() and parts.fragment and target.suffix.casefold() == ".md":
                resolved = target.resolve()
                if resolved not in anchor_cache:
                    anchor_cache[resolved] = markdown_anchors(read_text(target))
                report.require(parts.fragment.casefold() in {item.casefold() for item in anchor_cache[resolved]}, rel(path), f"missing anchor #{parts.fragment} in {rel(target)}")


def sensitive_field_paths(value: Any, prefix: str = "$") -> list[str]:
    forbidden = re.compile(r"(?i)(secret|password|credential|token|accountkey|connectionstring|privatekey|clientsecret)")
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}"
            if forbidden.search(str(key)):
                found.append(path)
            found.extend(sensitive_field_paths(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(sensitive_field_paths(child, f"{prefix}[{index}]"))
    return found


def validate_progress_record(value: Any) -> list[str]:
    errors: list[str] = []
    schema_path = ROOT / "schemas/progress-schema.json"
    if not schema_path.is_file():
        return ["progress schema is missing"]
    schema = load_data(schema_path)
    assert schema is not None
    errors.extend("schema " + issue for issue in schema_issues(value, schema))
    if not isinstance(value, dict):
        return errors
    labs = value.get("labs", {})
    if isinstance(labs, dict):
        if set(labs) != set(EXPECTED_LABS):
            errors.append("labs must be exactly LAB-00 through LAB-27")
        for lab_id, record in labs.items():
            if not isinstance(record, dict):
                continue
            score = record.get("score")
            if lab_id in INSTRUCTIONAL_LABS:
                if score is not None and (type(score) is not int or not 0 <= score <= 50):
                    errors.append(f"{lab_id} score must be null or an integer from 0 through 50")
            elif "score" in record:
                errors.append(f"{lab_id} must not contain score")
    for path in sensitive_field_paths(value):
        errors.append(f"sensitive field is forbidden at {path}")
    return errors


def validate_progress_assets(report: Report) -> None:
    candidates = list((ROOT / "docs").rglob("*.js")) if (ROOT / "docs").is_dir() else []
    combined = "\n".join(read_text(path) for path in candidates)
    report.require("az305LearnerProgress.v1" in combined, "docs", "progress UI must use the fixed private browser-storage key")
    report.require(bool(re.search(r"256\s*\*\s*1024|262144", combined)), "docs", "progress import must enforce the 256 KiB limit")
    report.require("JSON.stringify" in combined and "JSON.parse" in combined, "docs", "progress UI must provide explicit JSON export and import")
    report.require(bool(re.search(r"(?i)sensitive|secret|password|credential|token", combined)), "docs", "progress UI must recursively reject sensitive fields")
    report.require(not re.search(r"(?i)fetch\s*\(|XMLHttpRequest|WebSocket", combined), "docs", "browser progress must not silently synchronize over a network")


class BuiltHtmlInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.has_title = False
        self.has_main = False
        self.lang = ""
        self.empty_alt = 0
        self.external_assets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {name.casefold(): value or "" for name, value in attrs}
        lowered = tag.casefold()
        if lowered == "html":
            self.lang = values.get("lang", "")
        elif lowered == "title":
            self.has_title = True
        elif lowered == "main" or values.get("role") == "main":
            self.has_main = True
        elif lowered == "img" and not values.get("alt", "").strip():
            self.empty_alt += 1
        if lowered in {"script", "img", "iframe", "video", "audio", "source"}:
            url = values.get("src", "")
            if url.startswith(("http://", "https://", "//")):
                self.external_assets.append(url)
        if lowered == "link" and "stylesheet" in values.get("rel", "").casefold():
            url = values.get("href", "")
            if url.startswith(("http://", "https://", "//")):
                self.external_assets.append(url)


def validate_built_site(site: Path, report: Report) -> None:
    html_files = sorted(site.rglob("*.html")) if site.is_dir() else []
    report.require(bool(html_files), rel(site), "built site contains no HTML pages")
    for path in html_files:
        parser = BuiltHtmlInspector()
        try:
            parser.feed(read_text(path))
        except Exception as exc:
            report.issue(rel(path), f"cannot inspect HTML: {exc}")
            continue
        report.require(parser.has_title, rel(path), "page has no title element")
        report.require(bool(parser.lang.strip()), rel(path), "page has no document language")
        report.require(parser.has_main, rel(path), "page has no main landmark")
        report.require(parser.empty_alt == 0, rel(path), f"page has {parser.empty_alt} image(s) without non-empty alt text")
        report.require(not parser.external_assets, rel(path), f"page loads external active assets: {parser.external_assets}")


def validate_portable_copies(labs: dict[str, dict[str, Any]], report: Report) -> None:
    with tempfile.TemporaryDirectory(prefix="az305-portability-") as temp_name:
        destination_root = Path(temp_name)
        for lab_id, lab in labs.items():
            source = ROOT / "labs" / str(lab.get("folder", ""))
            if not source.is_dir():
                continue
            destination = destination_root / source.name
            shutil.copytree(source, destination)
            track = str(lab.get("track"))
            required = [
                destination / "lab.yml",
                destination / "design/requirements.yml",
                destination / "design/decision.yml",
                destination / "diagrams/architecture.mmd",
                destination / "diagrams/architecture.svg",
                destination / "README.md",
                destination / "solution/README.md",
                destination / "tests/Contract.Tests.ps1",
                *(destination / "scripts" / track / name for name in LIFECYCLE_SCRIPTS),
            ]
            report.require(all(path.is_file() for path in required), lab_id, "isolated copy lacks one or more self-contained required artifacts")
            for path in destination.joinpath("scripts", track).glob("*.ps1") if destination.joinpath("scripts", track).is_dir() else []:
                text = read_text(path)
                report.require("curriculum/" not in text and "tools/" not in text and "$PSScriptRoot/../../" not in text, lab_id, f"{path.name} depends on the repository root")


def validate_current_service_guidance(report: Report) -> None:
    paths = [ROOT / "curriculum/lab-content.yml"]
    paths.extend((ROOT / "labs").glob("*/README.md"))
    corpus = "\n".join(read_text(path) for path in paths if path.is_file()).casefold()
    requirements = {
        "Microsoft Entra External ID": ("external id",),
        "Azure Managed Redis": ("azure managed redis",),
        "Azure Monitor Agent with DCR/DCRA": ("azure monitor agent", "dcr", "dcra"),
        "Standard Load Balancer outbound design": ("standard load balancer", "outbound"),
        "Front Door Standard/Premium": ("front door", "standard", "premium"),
    }
    for label, needles in requirements.items():
        report.require(all(needle in corpus for needle in needles), "curriculum/lab-content.yml", f"current-service guidance missing: {label}")


def run_validation(site: Path | None = None, portability: bool = True) -> Report:
    report = Report()
    validate_schema_contracts(report)
    models = validate_source_models(report)
    if models:
        blueprint, catalog, content, sources, commands = models
        official, labs, content_by_id = validate_counts_and_mapping(blueprint, catalog, content, report)
        validate_architecture_specificity(labs, content_by_id, report)
        validate_markers_and_layout(labs, report)
        validate_generated_schemas(labs, report)
        validate_traceability_and_labs(official, labs, sources, report)
        validate_lane_commands(labs, content_by_id, commands, report)
        validate_readmes_and_sync(labs, report)
        validate_lifecycle_contracts(labs, report)
        validate_assessment_totals(labs, report)
        validate_diagrams(labs, report)
        validate_bicep_files(labs, report)
        if portability:
            validate_portable_copies(labs, report)
    validate_repository_hygiene(report)
    validate_internal_links(report)
    validate_workflows(report)
    validate_progress_assets(report)
    validate_current_service_guidance(report)
    if site is not None:
        validate_built_site(site, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable results")
    parser.add_argument("--site", type=Path, help="Also inspect a built MkDocs site")
    parser.add_argument("--skip-portability", action="store_true", help="Skip temporary isolated-copy checks")
    args = parser.parse_args()
    site = args.site.resolve() if args.site else None
    report = run_validation(site=site, portability=not args.skip_portability)
    if args.json:
        print(json.dumps({"passed": not report.issues, "checks": report.checks, "issueCount": len(report.issues), "issues": report.issues}, indent=2))
    elif report.issues:
        print(f"repository validation failed: {len(report.issues)} issue(s) across {report.checks} checks")
        for issue in report.issues:
            print(f"- {issue}")
    else:
        print(f"repository validation passed: {report.checks} checks")
    return 1 if report.issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
