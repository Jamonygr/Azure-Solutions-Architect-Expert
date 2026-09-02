from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from validate_repository import Report, validate_architecture_specificity


def models() -> tuple[dict, dict]:
    catalog = yaml.safe_load((ROOT / "curriculum/catalog.yml").read_text(encoding="utf-8")) if (ROOT / "curriculum/catalog.yml").exists() else yaml.safe_load((ROOT / "curriculum/lab-catalog.yml").read_text(encoding="utf-8"))
    content = yaml.safe_load((ROOT / "curriculum/lab-content.yml").read_text(encoding="utf-8"))
    labs = {item["id"]: item for item in catalog["labs"]}
    content_by_id = {f"LAB-{item['number']}": item for item in content["labs"]}
    return labs, content_by_id


class ArchitectureContentTests(unittest.TestCase):
    def test_reviewed_architecture_content_passes_specificity_gate(self) -> None:
        labs, content = models()
        report = Report()
        validate_architecture_specificity(labs, content, report)
        self.assertEqual(report.issues, [])

    def test_generic_scaffold_is_rejected(self) -> None:
        labs, content = models()
        content = copy.deepcopy(content)
        content["LAB-00"]["architectureAnalysis"]["risks"][0]["risk"] = "The design may be overfit to the initial workload profile."
        report = Report()
        validate_architecture_specificity(labs, content, report)
        self.assertTrue(any("generic architecture scaffold" in issue for issue in report.issues))

    def test_cross_lab_fact_duplication_is_rejected(self) -> None:
        labs, content = models()
        content = copy.deepcopy(content)
        content["LAB-01"]["architectureAnalysis"]["facts"]["data"] = content["LAB-00"]["architectureAnalysis"]["facts"]["data"]
        report = Report()
        validate_architecture_specificity(labs, content, report)
        self.assertTrue(any("repeated exact fact:data" in issue for issue in report.issues))

    def test_three_eligible_and_one_disqualified_are_required(self) -> None:
        labs, content = models()
        content = copy.deepcopy(content)
        content["LAB-02"]["architectureAnalysis"]["candidateAnalyses"] = content["LAB-02"]["architectureAnalysis"]["candidateAnalyses"][:3]
        report = Report()
        validate_architecture_specificity(labs, content, report)
        self.assertTrue(any("specifically disqualified" in issue for issue in report.issues))

    def test_duplicate_complete_score_profile_is_rejected(self) -> None:
        labs, content = models()
        content = copy.deepcopy(content)
        source = content["LAB-00"]["architectureAnalysis"]["candidateAnalyses"]
        target = content["LAB-01"]["architectureAnalysis"]["candidateAnalyses"]
        for source_candidate, target_candidate in zip(source, target):
            target_candidate["scores"] = copy.deepcopy(source_candidate["scores"])
        report = Report()
        validate_architecture_specificity(labs, content, report)
        self.assertTrue(any("score profile duplicates" in issue for issue in report.issues))

    def test_revised_selection_must_remain_eligible(self) -> None:
        labs, content = models()
        content = copy.deepcopy(content)
        analysis = content["LAB-03"]["architectureAnalysis"]
        analysis["revisedDecision"]["selectedCandidate"] = analysis["candidateAnalyses"][-1]["name"]
        report = Report()
        validate_architecture_specificity(labs, content, report)
        self.assertTrue(any("revised selection must name an eligible" in issue for issue in report.issues))

    def test_generated_requirements_preserve_authored_facts(self) -> None:
        labs, content = models()
        for lab_id, lab in labs.items():
            folder = ROOT / "labs" / lab["folder"] / "design" / "requirements.yml"
            generated = yaml.safe_load(folder.read_text(encoding="utf-8"))
            analysis = content[lab_id]["architectureAnalysis"]
            self.assertEqual(generated["facts"], analysis["facts"], lab_id)
            self.assertEqual(generated["constraints"][:2], analysis["constraints"], lab_id)
            self.assertEqual(generated["assumptions"][:2], analysis["assumptions"], lab_id)
            self.assertEqual(generated["changeRequest"]["expectedRevision"], analysis["changeExpectedRevision"], lab_id)

    def test_generated_decisions_preserve_authored_analysis(self) -> None:
        labs, content = models()
        for lab_id, lab in labs.items():
            path = ROOT / "labs" / lab["folder"] / "design" / "decision.yml"
            generated = yaml.safe_load(path.read_text(encoding="utf-8"))
            analysis = content[lab_id]["architectureAnalysis"]
            authored = {item["name"]: item for item in analysis["candidateAnalyses"]}
            self.assertEqual(generated["selectedCandidate"], content[lab_id]["selected"], lab_id)
            self.assertEqual(generated["risks"], analysis["risks"], lab_id)
            self.assertEqual(generated["waf"], analysis["waf"], lab_id)
            self.assertEqual(generated["safeAnalogue"], analysis["safeAnalogue"], lab_id)
            self.assertEqual(generated["revisedDecision"]["waf"], analysis["revisedDecision"]["waf"], lab_id)
            for candidate in generated["candidates"]:
                source = authored[candidate["name"]]
                self.assertEqual(candidate["scores"], source["scores"], lab_id)
                self.assertEqual(candidate["eligible"], source["eligible"], lab_id)
                self.assertEqual(candidate["disqualifiers"], source["disqualifiers"], lab_id)
                self.assertEqual(candidate["rationale"], source["rationale"], lab_id)


if __name__ == "__main__":
    unittest.main()
