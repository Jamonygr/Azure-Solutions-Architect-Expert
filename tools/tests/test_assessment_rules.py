from __future__ import annotations

import sys
import unittest
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from generate_assessment_banks import answer_sequence, make_bank
from validate_assessments import (
    BANNED_GENERATOR_SCAFFOLDS,
    checkpoint_specific_vocabulary,
    context_skeleton,
    context_vocabulary,
    decamouflaged,
    max_run,
    normalized,
    repeated_frames,
    repeated_cross_bank_leadins,
    repeated_ngrams,
    short_period,
    token_overlap,
    word_count,
)


class AssessmentRuleTests(unittest.TestCase):
    def test_answer_sequence_is_balanced_and_non_periodic(self) -> None:
        values = answer_sequence("LAB-11")
        self.assertEqual(sorted(Counter(values).values()), [12, 12, 13, 13])
        self.assertLessEqual(max_run(values), 3)
        self.assertIsNone(short_period(values))

    def test_overlap_and_normalization_support_near_duplicate_rule(self) -> None:
        left = "Choose a resilient regional architecture with private connectivity and measured recovery."
        right = "Choose a resilient regional architecture with private connectivity and tested recovery."
        self.assertGreaterEqual(token_overlap(left, right), 0.82)
        self.assertGreaterEqual(SequenceMatcher(None, normalized(left), normalized(right)).ratio(), 0.88)
        self.assertEqual(normalized("A, B; C!"), "a b c")

    def test_known_short_period_and_answer_run_are_rejected_by_primitives(self) -> None:
        self.assertEqual(short_period(list("AB" * 25)), 2)
        self.assertGreater(max_run(list("AAAABCD")), 3)

    def test_decamouflage_removes_identifiers_variables_numbers_and_old_suffix(self) -> None:
        left = "Use the safe evidence — apply this specifically to LAB-01 checkpoint 3."
        right = "Use the safe evidence — apply this specifically to LAB-22 checkpoint 5."
        self.assertEqual(decamouflaged(left), decamouflaged(right))
        self.assertEqual(decamouflaged("LAB01-Q07 runs $WorkspaceName 30 times"), "identifier runs variable number times")

    def test_context_masking_exposes_a_repeated_service_name_template(self) -> None:
        checkpoint_a = {"title": "Route telemetry", "expected": "Logs reach the regional workspace"}
        checkpoint_b = {"title": "Partition tenant documents", "expected": "Tenants use a hierarchical key"}
        lab_a = {"title": "Monitor design", "laneLabel": "Azure CLI"}
        lab_b = {"title": "NoSQL design", "laneLabel": "Azure CLI"}
        content_a = {"scenario": "Contoso routes platform telemetry.", "businessOutcome": "Faster incident review", "stakeholders": ["Operations"], "candidates": ["Regional workspace"], "selected": "Regional workspace", "changeRequest": "Retain records longer", "checkpoints": [checkpoint_a]}
        content_b = {"scenario": "Fabrikam partitions tenant records.", "businessOutcome": "Predictable scale", "stakeholders": ["Data team"], "candidates": ["Hierarchical key"], "selected": "Hierarchical key", "changeRequest": "Increase tenants", "checkpoints": [checkpoint_b]}
        first = "In the Monitor design review, which recommendation most directly satisfies Route telemetry?"
        second = "In the NoSQL design review, which recommendation most directly satisfies Partition tenant documents?"
        frame_a = context_skeleton(first, context_vocabulary(lab_a, content_a, checkpoint_a))
        frame_b = context_skeleton(second, context_vocabulary(lab_b, content_b, checkpoint_b))
        self.assertEqual(frame_a, frame_b)
        self.assertIn(frame_a, repeated_frames([("Q1", frame_a), ("Q2", frame_b), ("Q3", frame_a)], 3))

    def test_cross_bank_option_leadin_rejects_a_long_repeated_opening(self) -> None:
        opening = "Inspect the recorded properties and independently compare every expected field before accepting the proposed architecture for production use"
        values = [
            ("LAB-01", "LAB01-Q01/A", opening + " in region alpha"),
            ("LAB-02", "LAB02-Q01/B", opening + " in region beta"),
            ("LAB-02", "LAB02-Q02/C", opening + " in region gamma"),
        ]
        self.assertTrue(repeated_cross_bank_leadins(values))

    def test_malformed_pair_scaffolds_are_banned(self) -> None:
        malformed = (
            "After declare the scope, exclude credentials.",
            "Complete store the record. Then inspect it.",
            "Complete this action: record the ID.",
            "Complete two checks: inspect; exclude.",
            "Inspect the output; follow with exclude secrets.",
        )
        for text in malformed:
            self.assertTrue(any(pattern.search(text) for pattern in BANNED_GENERATOR_SCAFFOLDS), text)

    def test_bank_generator_is_deterministic_with_exact_mix_and_mappings(self) -> None:
        catalog = yaml.safe_load((ROOT / "curriculum/lab-catalog.yml").read_text(encoding="utf-8"))
        content = yaml.safe_load((ROOT / "curriculum/lab-content.yml").read_text(encoding="utf-8"))
        lab = next(item for item in catalog["labs"] if item["id"] == "LAB-01")
        authored = next(item for item in content["labs"] if str(item["number"]).zfill(2) == "01")
        first = make_bank(lab, authored)
        second = make_bank(lab, authored)
        self.assertEqual(first, second)
        self.assertEqual(len(first["questions"]), 50)
        self.assertEqual(Counter(item["difficulty"] for item in first["questions"]), Counter({"foundational": 15, "applied": 25, "advanced": 10}))
        self.assertEqual(sorted(Counter(item["checkpointId"] for item in first["questions"]).values()), [10, 10, 10, 10, 10])
        self.assertTrue(all(item["objectiveId"] in lab["primaryObjectiveIds"] for item in first["questions"]))
        self.assertTrue(all(item["id"] not in item["stem"] for item in first["questions"]))
        self.assertTrue(all("apply this specifically" not in option.lower() for item in first["questions"] for option in item["options"].values()))
        frames = []
        for item in first["questions"]:
            checkpoint_number = int(item["checkpointId"][-1])
            checkpoint = authored["checkpoints"][checkpoint_number - 1]
            vocabulary = context_vocabulary(lab, authored, checkpoint)
            frames.append((item["id"], context_skeleton(item["stem"], vocabulary)))
        self.assertEqual(repeated_frames(frames, 3), {})
        for item in first["questions"]:
            checkpoint = authored["checkpoints"][int(item["checkpointId"][-1]) - 1]
            keyed_terms = set(decamouflaged(item["options"][item["answer"]]).split())
            self.assertTrue(keyed_terms.intersection(checkpoint_specific_vocabulary(checkpoint)), item["id"])
            self.assertLessEqual(word_count(item["stem"]), 70, item["id"])
            self.assertTrue(all(word_count(option) <= 55 for option in item["options"].values()), item["id"])
            self.assertFalse(any(pattern.search(text) for pattern in BANNED_GENERATOR_SCAFFOLDS for text in item["options"].values()), item["id"])
        self.assertEqual(repeated_ngrams([(item["id"], item["stem"]) for item in first["questions"]]), {})


if __name__ == "__main__":
    unittest.main()
