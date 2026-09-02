"""Regression tests for the registered visual learning environment."""

from __future__ import annotations

import hashlib
import json
import struct
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[2]


class VisualContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = yaml.safe_load((ROOT / "curriculum/visuals.yml").read_text(encoding="utf-8"))

    def test_registry_is_closed_and_valid(self) -> None:
        schema = json.loads((ROOT / "schemas/visual-registry-schema.json").read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual([], list(Draft202012Validator(schema).iter_errors(self.registry)))

    def test_fixed_visual_counts_and_lab_coverage(self) -> None:
        self.assertEqual(7, len(self.registry["rasterAssets"]))
        self.assertEqual(16, len(self.registry["siteInfographics"]))
        self.assertEqual([f"LAB-{number:02d}" for number in range(28)], [item["id"] for item in self.registry["labs"]])
        self.assertEqual(84, len(list((ROOT / "labs").glob("*/diagrams/*.svg"))))
        self.assertEqual(28, len(list((ROOT / "labs").glob("*/diagrams/*.mmd"))))
        self.assertEqual(16, len(list((ROOT / "docs/site-assets/infographics").glob("*.svg"))))

    def test_topologies_are_specific_and_fully_labelled(self) -> None:
        signatures = set()
        for lab in self.registry["labs"]:
            topology = lab["topology"]
            signature = json.dumps({"nodes": topology["nodes"], "edges": topology["edges"]}, sort_keys=True)
            self.assertNotIn(signature, signatures, lab["id"])
            signatures.add(signature)
            node_ids = {node["id"] for node in topology["nodes"]}
            self.assertGreaterEqual(len(node_ids), 4)
            self.assertTrue(all(edge["from"] in node_ids and edge["to"] in node_ids and edge["label"] for edge in topology["edges"]))
            folder = ROOT / "labs" / lab["folder"]
            source = (folder / "diagrams/architecture.mmd").read_text(encoding="utf-8")
            svg = (folder / "diagrams/architecture.svg").read_text(encoding="utf-8")
            self.assertNotIn("Independent positive and negative evidence", source)
            self.assertEqual(len(topology["nodes"]), svg.count('aria-label="Service node:'))

    def test_decisions_timelines_and_waf_cards_are_complete(self) -> None:
        for lab in self.registry["labs"]:
            folder = ROOT / "labs" / lab["folder"]
            decision = yaml.safe_load((folder / "design/decision.yml").read_text(encoding="utf-8"))
            decision_svg = (folder / "diagrams/decision-matrix.svg").read_text(encoding="utf-8")
            readme = (folder / "README.md").read_text(encoding="utf-8")
            self.assertEqual(len(decision["candidates"]), decision_svg.count('aria-label="Candidate '), lab["id"])
            self.assertEqual(5, readme.count('<li><a href="#checkpoint-'), lab["id"])
            self.assertEqual(5, readme.count('class="az305-waf-card"'), lab["id"])

    def test_manifest_hashes_and_raster_metadata(self) -> None:
        manifest = json.loads((ROOT / self.registry["generatedManifestPath"]).read_text(encoding="utf-8"))
        self.assertEqual({"registeredRasters": 7, "labSvgs": 84, "siteInfographics": 16}, {key: manifest["counts"][key] for key in ("registeredRasters", "labSvgs", "siteInfographics")})
        for asset in manifest["assets"]:
            path = ROOT / asset["path"]
            payload = path.read_bytes()
            self.assertEqual(len(payload), asset["byteSize"], asset["path"])
            self.assertEqual(hashlib.sha256(payload).hexdigest(), asset["sha256"], asset["path"])
        for raster in self.registry["rasterAssets"]:
            payload = (ROOT / raster["path"]).read_bytes()
            self.assertEqual((1536, 1024), struct.unpack(">II", payload[16:24]))
            position = 8
            while position + 12 <= len(payload):
                size = struct.unpack(">I", payload[position:position + 4])[0]
                chunk_type = payload[position + 4:position + 8]
                self.assertEqual(0, chunk_type[0] & 32, f"ancillary metadata in {raster['path']}")
                position += size + 12


if __name__ == "__main__":
    unittest.main()
