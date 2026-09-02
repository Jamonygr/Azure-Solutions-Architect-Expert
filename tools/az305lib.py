"""Shared deterministic helpers for the AZ-305 offline toolchain."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "1.0.0"
BEGIN = "BEGIN GENERATED AZ305 V1"
END = "END GENERATED AZ305 V1"


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected a mapping in {path.relative_to(ROOT)}")
    return data


def load_model() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    return (
        load_yaml(ROOT / "curriculum/blueprint.yml"),
        load_yaml(ROOT / "curriculum/lab-catalog.yml"),
        load_yaml(ROOT / "curriculum/lab-content.yml"),
        load_yaml(ROOT / "curriculum/sources.yml"),
        load_yaml(ROOT / "curriculum/commands.yml"),
    )


def objective_map(blueprint: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result = {item["id"]: item for item in blueprint["foundationObjectives"]}
    for domain in blueprint["domains"]:
        for group in domain["groups"]:
            for objective in group["objectives"]:
                result[objective["id"]] = objective
    return result


def domain_name(domain_id: str) -> str:
    return {
        "FOUNDATION": "foundation",
        "IGM": "identity-governance-monitoring",
        "DATA": "data",
        "BC": "business-continuity",
        "INF": "infrastructure",
        "CAPSTONE": "capstone",
    }[domain_id]


def yaml_text(value: Any) -> str:
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=110).rstrip() + "\n"


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def marker_lines(style: str) -> tuple[str, str]:
    wrappers = {
        "markdown": (f"<!-- {BEGIN} -->", f"<!-- {END} -->"),
        "powershell": (f"# {BEGIN}", f"# {END}"),
        "yaml": (f"# {BEGIN}", f"# {END}"),
        "mermaid": (f"%% {BEGIN}", f"%% {END}"),
        "bicep": (f"// {BEGIN}", f"// {END}"),
        "xml": (f"<!-- {BEGIN} -->", f"<!-- {END} -->"),
        "json": (f'  "_generatedBegin": "{BEGIN}",', f'  "_generatedEnd": "{END}"'),
    }
    return wrappers[style]


def compose_generated(body: str, style: str) -> str:
    begin, end = marker_lines(style)
    normalized = body.rstrip("\n")
    return f"{begin}\n{normalized}\n{end}\n"


def merge_generated(existing: str, body: str, style: str) -> str:
    begin, end = marker_lines(style)
    begin_count = existing.count(BEGIN)
    end_count = existing.count(END)
    if begin_count != 1 or end_count != 1:
        raise ValueError(
            f"Generated file must contain exactly one {BEGIN!r} and one {END!r}; "
            f"found {begin_count} and {end_count}"
        )
    start = existing.find(begin)
    finish = existing.find(end)
    if start < 0 or finish < 0 or finish <= start:
        raise ValueError("Generated markers are malformed, out of order, or use the wrong comment style")
    start_content = start + len(begin)
    if BEGIN in existing[start_content:finish] or END in existing[start_content:finish]:
        raise ValueError("Nested generated markers are not allowed")
    replacement = "\n" + body.rstrip("\n") + "\n"
    return existing[:start_content] + replacement + existing[finish:]


def plan_generated(path: Path, body: str, style: str) -> str:
    if not path.exists():
        return compose_generated(body, style)
    existing = path.read_text(encoding="utf-8")
    return merge_generated(existing, body, style)


def write_or_check(path: Path, body: str, style: str, check: bool) -> bool:
    expected = plan_generated(path, body, style)
    actual = path.read_text(encoding="utf-8") if path.exists() else ""
    if actual == expected:
        return False
    if check:
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(expected)
    return True


def ps_single(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")
