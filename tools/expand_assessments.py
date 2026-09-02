#!/usr/bin/env python3
"""Render learner-only questions and complete answer keys from questions.yml."""

from __future__ import annotations

import argparse

from az305lib import ROOT, load_model, load_yaml, write_or_check


def learner_markdown(bank: dict) -> str:
    parts = [f"# {bank['labId']} learner assessment", "", "Choose one answer for each item. This page intentionally contains no answers or explanations."]
    for question in bank["questions"]:
        parts.extend(["", f"## {question['id']} — {question['difficulty']}", "", question["stem"], ""])
        for letter, option in question["options"].items():
            parts.append(f"- {letter}. {option}")
    return "\n".join(parts) + "\n"


def answer_markdown(bank: dict) -> str:
    parts = [f"# {bank['labId']} answer key", "", "Use after completing the learner assessment. Every choice has a specific explanation."]
    for question in bank["questions"]:
        parts.extend(["", f"## {question['id']} — answer {question['answer']}", "", question["stem"], ""])
        for letter, option in question["options"].items():
            marker = "✓" if letter == question["answer"] else "✗"
            parts.append(f"- {marker} **{letter}. {option}** — {question['explanations'][letter]}")
        parts.extend(["", f"Remediation: [{question['remediationAnchor']}](../README.md#{question['remediationAnchor']})", "", f"Source: {question['source']} (verified {question['verifiedOn']})"])
    return "\n".join(parts) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--only", nargs="*", default=[])
    args = parser.parse_args()
    _, catalog, _, _, _ = load_model()
    only = set(args.only)
    drift = []
    for lab in catalog["labs"]:
        if not 1 <= int(lab["number"]) <= 25 or (only and lab["id"] not in only):
            continue
        folder = ROOT / "labs" / lab["folder"] / "assessment"
        bank = load_yaml(folder / "questions.yml")
        for filename, body in (("QUESTIONS.md", learner_markdown(bank)), ("ANSWERS.md", answer_markdown(bank))):
            path = folder / filename
            if write_or_check(path, body, "markdown", args.check):
                drift.append(str(path.relative_to(ROOT)))
    if drift and args.check:
        print("Rendered assessment drift:\n" + "\n".join(f"- {item}" for item in drift))
        return 1
    print(f"{'would update' if args.check else 'updated' if drift else 'verified'} {len(drift)} assessment pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
