#!/usr/bin/env python3
"""Assemble reviewed domain fragments into the authoritative lab-content file."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FRAGMENTS = (
    ROOT / "curriculum/content/foundation.yml",
    ROOT / "curriculum/content/igm-data.yml",
    ROOT / "curriculum/content/bc-infrastructure.yml",
)
ANALYSIS = ROOT / "curriculum/content/architecture-analysis.yml"
TARGET = ROOT / "curriculum/lab-content.yml"


def render() -> str:
    labs: list[dict] = []
    for path in FRAGMENTS:
        if not path.exists():
            raise SystemExit(f"Missing content fragment: {path.relative_to(ROOT)}")
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if data.get("schemaVersion") != "1.0.0" or not isinstance(data.get("labs"), list):
            raise SystemExit(f"Invalid content fragment: {path.relative_to(ROOT)}")
        labs.extend(data["labs"])
    numbers = [str(lab.get("number", "")).zfill(2) for lab in labs]
    if numbers != [f"{index:02d}" for index in range(28)]:
        raise SystemExit(f"Lab fragments must form the ordered 00-27 sequence; found {numbers}")
    if not ANALYSIS.exists():
        raise SystemExit(f"Missing architecture analysis fragment: {ANALYSIS.relative_to(ROOT)}")
    analysis_data = yaml.safe_load(ANALYSIS.read_text(encoding="utf-8"))
    analysis_labs = analysis_data.get("labs", []) if isinstance(analysis_data, dict) else []
    if analysis_data.get("schemaVersion") != "1.0.0" or not isinstance(analysis_labs, list):
        raise SystemExit(f"Invalid architecture analysis fragment: {ANALYSIS.relative_to(ROOT)}")
    analysis_by_number = {
        str(item.get("number", "")).zfill(2): item.get("architectureAnalysis")
        for item in analysis_labs
        if isinstance(item, dict)
    }
    expected = {f"{index:02d}" for index in range(28)}
    if set(analysis_by_number) != expected or len(analysis_labs) != 28:
        raise SystemExit("Architecture analysis fragment must contain each LAB-00 through LAB-27 exactly once")
    for lab in labs:
        number = str(lab["number"]).zfill(2)
        analysis = analysis_by_number[number]
        if not isinstance(analysis, dict):
            raise SystemExit(f"LAB-{number} architectureAnalysis must be an object")
        lab["architectureAnalysis"] = analysis
    header = (
        "# Authoritative authored content assembled from reviewed domain and architecture-analysis fragments.\n"
        "# Run tools/merge_lab_content.py --check to detect drift.\n"
    )
    return header + yaml.safe_dump(
        {"schemaVersion": "1.0.0", "labs": labs},
        sort_keys=False,
        allow_unicode=True,
        width=120,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        actual = TARGET.read_text(encoding="utf-8") if TARGET.exists() else ""
        if actual != expected:
            print("curriculum/lab-content.yml is out of date")
            return 1
        print("lab-content assembly is current")
        return 0
    with TARGET.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(expected)
    print("wrote curriculum/lab-content.yml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
