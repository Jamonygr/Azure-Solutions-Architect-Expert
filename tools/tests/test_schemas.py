from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from validate_repository import SCHEMA_VERSION, schema_issues


class SchemaContractTests(unittest.TestCase):
    def test_all_schemas_are_closed_draft_2020_12_with_local_urns(self) -> None:
        schemas = sorted((ROOT / "schemas").glob("*-schema.json"))
        self.assertGreaterEqual(len(schemas), 13)
        identifiers: set[str] = set()
        for path in schemas:
            schema = json.loads(path.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
            self.assertTrue(schema["$id"].startswith("urn:az305:schema:"))
            self.assertTrue(schema["$id"].endswith(":" + SCHEMA_VERSION))
            self.assertFalse(schema["additionalProperties"])
            self.assertNotIn(schema["$id"], identifiers)
            identifiers.add(schema["$id"])

    def test_closed_schema_rejects_unknown_root_property(self) -> None:
        schema = json.loads((ROOT / "schemas/progress-schema.json").read_text(encoding="utf-8"))
        record = {
            "schemaVersion": "1.0.0",
            "exportedAt": "2026-09-02T00:00:00Z",
            "labs": {},
            "unexpected": True,
        }
        for index in range(28):
            item = {"completed": False, "checkpoints": [False] * 5}
            if 1 <= index <= 25:
                item["score"] = None
            record["labs"][f"LAB-{index:02d}"] = item
        self.assertTrue(any("Additional properties" in issue for issue in schema_issues(record, schema)))

    def test_schema_rejects_wrong_version(self) -> None:
        schema = json.loads((ROOT / "schemas/questions-schema.json").read_text(encoding="utf-8"))
        self.assertTrue(schema_issues({"schemaVersion": "2.0.0", "labId": "LAB-01", "questions": []}, schema))


if __name__ == "__main__":
    unittest.main()
