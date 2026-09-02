from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from validate_repository import Report, sensitive_field_paths, validate_decision, validate_progress_record


def progress_record() -> dict:
    record = {
        "schemaVersion": "1.0.0",
        "exportedAt": "2026-09-02T00:00:00Z",
        "labs": {},
    }
    for index in range(28):
        item = {"completed": False, "checkpoints": [False, False, False, False, False]}
        if 1 <= index <= 25:
            item["score"] = 0
        record["labs"][f"LAB-{index:02d}"] = item
    return record


def decision_fixture() -> tuple[dict, dict, dict]:
    criteria = [
        {"id": "C1", "name": "Fit", "weight": 50},
        {"id": "C2", "name": "Reliability", "weight": 30},
        {"id": "C3", "name": "Cost", "weight": 20},
    ]
    candidates = []
    for index, (name, scores) in enumerate((("A", {"C1": 5, "C2": 5, "C3": 4}), ("B", {"C1": 4, "C2": 4, "C3": 4}), ("C", {"C1": 3, "C2": 3, "C3": 3}), ("D", {"C1": 1, "C2": 2, "C3": 1}))):
        candidates.append({
            "id": f"CAND-{name}", "name": name, "eligible": name != "D",
            "disqualifiers": [] if name != "D" else ["Violates a mandatory architecture boundary"],
            "scores": scores, "weightedTotal": sum(item["weight"] * scores[item["id"]] for item in criteria) / 5,
            "rationale": f"Candidate {name} has a measurable architecture fit.",
        })
    requirements = {
        "functionalRequirements": [{"id": "LAB01-REQ-01", "mandatory": True, "objectiveIds": ["IGM-LOG-01"]}],
        "nonfunctionalRequirements": [],
        "changeRequest": {"id": "LAB01-CR-01"},
    }
    decision = {
        "criteria": criteria, "candidates": candidates, "selectedCandidate": "A",
        "rejectedAlternatives": [{"candidate": "B"}, {"candidate": "C"}, {"candidate": "D"}],
        "waf": {
            "reliability": "x", "security": "x", "costOptimization": "x",
            "operationalExcellence": "x", "performanceEfficiency": "x",
        },
        "safeAnalogue": None, "implementationMode": "reference-deployable",
        "adr": {"id": "ADR-LAB01-001"},
        "revisedDecision": {
            "changeRequestId": "LAB01-CR-01", "mandatoryRequirementId": "LAB01-REQ-01",
            "reason": "LAB01-REQ-01 is now the mandatory basis for the documented revision.",
            "selectedCandidate": "A",
            "waf": {
                "reliability": "x", "security": "x", "costOptimization": "x",
                "operationalExcellence": "x", "performanceEfficiency": "x",
            },
        },
    }
    lab = {"id": "LAB-01", "number": "01", "implementationMode": "reference-deployable"}
    return decision, requirements, lab


class TraceabilityAndProgressTests(unittest.TestCase):
    def test_progress_accepts_exact_28_lab_shape(self) -> None:
        self.assertEqual(validate_progress_record(progress_record()), [])

    def test_progress_rejects_score_on_non_assessment_lab(self) -> None:
        record = progress_record()
        record["labs"]["LAB-27"]["score"] = 1
        self.assertTrue(any("LAB-27 must not contain score" in item for item in validate_progress_record(record)))

    def test_recursive_sensitive_field_rejection(self) -> None:
        record = progress_record()
        record["labs"]["LAB-01"]["notes"] = {"access" + "Token": "not-a-real-value"}
        paths = sensitive_field_paths(record)
        self.assertEqual(paths, ["$.labs.LAB-01.notes.accessToken"])
        self.assertTrue(any("sensitive field" in item for item in validate_progress_record(record)))

    def test_decision_arithmetic_and_override_trace_pass(self) -> None:
        decision, requirements, lab = decision_fixture()
        report = Report()
        validate_decision(decision, requirements, lab, report)
        self.assertEqual(report.issues, [])

    def test_decision_bad_math_and_disqualifier_fail(self) -> None:
        decision, requirements, lab = decision_fixture()
        decision["candidates"][0]["weightedTotal"] = 99
        decision["candidates"][0]["disqualifiers"] = ["Violates mandatory boundary"]
        report = Report()
        validate_decision(decision, requirements, lab, report)
        self.assertTrue(any("weighted total" in item for item in report.issues))
        self.assertTrue(any("disqualified candidate" in item for item in report.issues))


if __name__ == "__main__":
    unittest.main()
