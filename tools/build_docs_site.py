#!/usr/bin/env python3
"""Stage the deterministic, answer-free MkDocs source tree."""

from __future__ import annotations

import argparse
import html
import re
import shutil
import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "site"
ASSETS = ROOT / "docs" / "site-assets"
STAGE = ROOT / ".site-docs"
CATALOG_BEGIN = "<!-- BEGIN GENERATED AZ305 DOCS CATALOG -->"
CATALOG_END = "<!-- END GENERATED AZ305 DOCS CATALOG -->"
OBJECTIVES_BEGIN = "<!-- BEGIN GENERATED AZ305 DOCS OBJECTIVES -->"
OBJECTIVES_END = "<!-- END GENERATED AZ305 DOCS OBJECTIVES -->"


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Expected a YAML mapping in {path.relative_to(ROOT)}")
    return data


def normalized_text(value: str) -> bytes:
    return (value.replace("\r\n", "\n").rstrip() + "\n").encode("utf-8")


def replace_region(source: str, begin: str, end: str, generated: str) -> str:
    if source.count(begin) != 1 or source.count(end) != 1:
        raise ValueError(f"Expected exactly one {begin}/{end} region")
    start = source.index(begin)
    finish = source.index(end, start) + len(end)
    if source.find(begin, start + len(begin), finish) != -1:
        raise ValueError(f"Nested generated region beginning {begin}")
    return source[:start] + begin + "\n" + generated.rstrip() + "\n" + end + source[finish:]


def catalog_markup(catalog: dict[str, Any]) -> str:
    rows = []
    for lab in catalog["labs"]:
        path = f"labs/{lab['folder']}/README.html"
        question_count = str(lab["questionCount"])
        if lab["questionCount"]:
            question_count = (
                f'<a href="labs/{html.escape(lab["folder"], quote=True)}/assessment/QUESTIONS.html">'
                f'{lab["questionCount"]}</a>'
            )
        cells = [
            f'<a href="{html.escape(path, quote=True)}"><strong>{html.escape(lab["id"])}</strong></a>',
            html.escape(lab["title"]),
            html.escape(lab["domainId"]),
            html.escape(lab["laneLabel"]),
            f'<code>{html.escape(lab["implementationMode"])}</code>',
            f'<span class="az305-status">{html.escape(lab["status"])}</span>',
            question_count,
        ]
        rows.append(
            '  <tr data-az305-catalog-row>'
            + "".join(f"<td>{cell}</td>" for cell in cells)
            + "</tr>"
        )
    return "\n".join(
        [
            '<div class="az305-table-scroll">',
            '<table>',
            "  <thead><tr><th>Lab</th><th>Title</th><th>Domain</th><th>Lane</th><th>Mode</th><th>Status</th><th>Questions</th></tr></thead>",
            "  <tbody>",
            *rows,
            "  </tbody>",
            "</table>",
            "</div>",
        ]
    )


def lab_directory(catalog: dict[str, Any]) -> str:
    lines = [
        "# Labs",
        "",
        "Each lab is portable and contains its own requirements, decision, diagram, lifecycle scripts, fixtures, tests, and solution rationale. Labs 01–25 also contain a learner-only assessment page on this site.",
        "",
        "| Lab | Title | Mode | Lane | Assessment |",
        "| --- | --- | --- | --- | --- |",
    ]
    for lab in catalog["labs"]:
        assessment = (
            f"[{lab['questionCount']} questions]({lab['folder']}/assessment/QUESTIONS.md)"
            if lab["questionCount"]
            else "Not scored"
        )
        lines.append(
            f"| [{lab['id']}]({lab['folder']}/README.md) | {lab['title']} | `{lab['implementationMode']}` | {lab['laneLabel']} | {assessment} |"
        )
    lines.extend(
        [
            "",
            "Use the [searchable catalog](../catalog.md) for domain and status filters. Answer keys are not staged in the documentation site.",
        ]
    )
    return "\n".join(lines)


def objective_markup(blueprint: dict[str, Any], catalog: dict[str, Any]) -> str:
    lab_by_id = {lab["id"]: lab for lab in catalog["labs"]}
    lines = [
        "## Foundation prerequisites (non-exam)",
        "",
        "| ID | Prerequisite | Primary lab | Status |",
        "| --- | --- | --- | --- |",
    ]
    for objective in blueprint["foundationObjectives"]:
        lab = lab_by_id[objective["primaryLab"]]
        lines.append(
            f"| `{objective['id']}` | {objective['title']} | [{lab['id']}](labs/{lab['folder']}/README.md) | `{lab['status']}` |"
        )
    for domain in blueprint["domains"]:
        lines.extend(
            [
                "",
                f"## {domain['name']} — {domain['weight']}",
                "",
                f"{domain['objectiveCount']} measured skills · {domain['instructionalLabCount']} instructional labs · {domain['questionCount']} questions",
                "",
                "| Objective | Official wording | Primary lab | Reinforcement | Status |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for group in domain["groups"]:
            for objective in group["objectives"]:
                lab = lab_by_id[objective["primaryLab"]]
                reinforcements = ", ".join(objective.get("reinforcementLabs", [])) or "—"
                lines.append(
                    f"| `{objective['id']}` | {objective['title']} | [{lab['id']}](labs/{lab['folder']}/README.md) | {reinforcements} | `{lab['status']}` |"
                )
    lines.extend(
        [
            "",
            f"Blueprint effective date: **{blueprint['exam']['blueprintEffectiveDate']}** · Source last updated: **{blueprint['exam']['sourceLastUpdated']}** · Research check: **{blueprint['exam']['researchedDate']}**",
        ]
    )
    return "\n".join(lines)


def expected_files() -> dict[Path, bytes]:
    blueprint = load_yaml(ROOT / "curriculum" / "blueprint.yml")
    catalog = load_yaml(ROOT / "curriculum" / "lab-catalog.yml")
    expected: dict[Path, bytes] = {}

    for path in sorted(SOURCE.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(SOURCE)
        if "answer" in relative.name.casefold():
            raise ValueError(f"Answer material is not permitted in docs/site: {relative}")
        text = path.read_text(encoding="utf-8")
        if relative.as_posix() == "catalog.md":
            text = replace_region(text, CATALOG_BEGIN, CATALOG_END, catalog_markup(catalog))
        elif relative.as_posix() == "objective-map.md":
            text = replace_region(text, OBJECTIVES_BEGIN, OBJECTIVES_END, objective_markup(blueprint, catalog))
        expected[relative] = normalized_text(text)

    for path in sorted(ASSETS.rglob("*")):
        if path.is_file():
            expected[Path("assets") / path.relative_to(ASSETS)] = path.read_bytes()

    expected[Path("labs") / "README.md"] = normalized_text(lab_directory(catalog))
    for lab in catalog["labs"]:
        source_lab = ROOT / "labs" / lab["folder"]
        readme = source_lab / "README.md"
        diagram = source_lab / "diagrams" / "architecture.svg"
        if not readme.is_file():
            raise FileNotFoundError(f"Missing generated lab README: {readme.relative_to(ROOT)}")
        if not diagram.is_file():
            raise FileNotFoundError(f"Missing generated architecture SVG: {diagram.relative_to(ROOT)}")
        base = Path("labs") / lab["folder"]
        number = int(lab["number"])
        lab_readme = readme.read_text(encoding="utf-8")
        if 1 <= number <= 25:
            lab_readme += (
                "\n\n---\n\n"
                "[Open the learner-only 50-question assessment](assessment/QUESTIONS.md). "
                "Its answer key is not present in this site.\n"
            )
        expected[base / "README.md"] = normalized_text(lab_readme)
        expected[base / "diagrams" / "architecture.svg"] = diagram.read_bytes()
        learner_questions = source_lab / "assessment" / "QUESTIONS.md"
        if 1 <= number <= 25:
            if not learner_questions.is_file():
                raise FileNotFoundError(f"Missing learner assessment: {learner_questions.relative_to(ROOT)}")
            expected[base / "assessment" / "QUESTIONS.md"] = normalized_text(
                learner_questions.read_text(encoding="utf-8")
            )
        elif learner_questions.exists():
            raise ValueError(f"Unscored {lab['id']} must not have a learner assessment")

    forbidden = [path for path in expected if "answer" in path.name.casefold()]
    if forbidden:
        raise ValueError("Answer-key path entered documentation staging: " + ", ".join(map(str, forbidden)))
    return expected


def active_external_assets(expected: dict[Path, bytes]) -> list[str]:
    patterns = [
        re.compile(r"<script\b[^>]*\bsrc=[\"']https?://", re.IGNORECASE),
        re.compile(r"<link\b[^>]*\bhref=[\"']https?://", re.IGNORECASE),
        re.compile(r"<(?:img|audio|video|source)\b[^>]*\bsrc=[\"']https?://", re.IGNORECASE),
        re.compile(r"url\(\s*[\"']?https?://", re.IGNORECASE),
    ]
    findings: list[str] = []
    for path, payload in expected.items():
        if path.suffix.casefold() not in {".md", ".html", ".css", ".js"}:
            continue
        text = payload.decode("utf-8")
        if any(pattern.search(text) for pattern in patterns):
            findings.append(path.as_posix())
    return findings


def existing_files() -> dict[Path, bytes]:
    if not STAGE.exists():
        return {}
    return {path.relative_to(STAGE): path.read_bytes() for path in sorted(STAGE.rglob("*")) if path.is_file()}


def drift(expected: dict[Path, bytes], actual: dict[Path, bytes]) -> list[str]:
    findings = []
    for path in sorted(expected.keys() - actual.keys()):
        findings.append(f"missing: {path.as_posix()}")
    for path in sorted(actual.keys() - expected.keys()):
        findings.append(f"unexpected: {path.as_posix()}")
    for path in sorted(expected.keys() & actual.keys()):
        if expected[path] != actual[path]:
            findings.append(f"changed: {path.as_posix()}")
    return findings


def assert_safe_stage() -> None:
    root = ROOT.resolve()
    stage = STAGE.resolve()
    if stage == root or root not in stage.parents or stage.name != ".site-docs":
        raise RuntimeError(f"Unsafe documentation staging path: {stage}")


def write_stage(expected: dict[Path, bytes]) -> None:
    assert_safe_stage()
    if STAGE.exists():
        shutil.rmtree(STAGE)
    for relative, payload in expected.items():
        destination = STAGE / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report staging drift without changing files")
    args = parser.parse_args()
    try:
        expected = expected_files()
        external = active_external_assets(expected)
        if external:
            print("External active assets are forbidden:\n" + "\n".join(f"- {path}" for path in external))
            return 1
        differences = drift(expected, existing_files())
        if args.check:
            if differences:
                print("Documentation staging drift:\n" + "\n".join(f"- {item}" for item in differences))
                return 1
            print(f"documentation staging is current ({len(expected)} files, no answer keys or external active assets)")
            return 0
        write_stage(expected)
        print(f"staged {len(expected)} documentation files without answer keys or external active assets")
        return 0
    except (FileNotFoundError, KeyError, TypeError, ValueError, RuntimeError, yaml.YAMLError) as error:
        print(f"documentation staging failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
