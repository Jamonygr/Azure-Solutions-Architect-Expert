from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from az305lib import BEGIN, END, compose_generated, merge_generated, write_or_check


class MarkerTests(unittest.TestCase):
    def test_merge_preserves_text_outside_markers(self) -> None:
        original = f"owner preface\n<!-- {BEGIN} -->\nold\n<!-- {END} -->\nowner suffix\n"
        merged = merge_generated(original, "new\ncontent", "markdown")
        self.assertTrue(merged.startswith("owner preface\n"))
        self.assertTrue(merged.endswith("owner suffix\n"))
        self.assertIn("\nnew\ncontent\n", merged)
        self.assertNotIn("\nold\n", merged)

    def test_missing_marker_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly one"):
            merge_generated("owner text only\n", "body", "markdown")

    def test_malformed_marker_order_is_rejected(self) -> None:
        malformed = f"<!-- {END} -->\nbody\n<!-- {BEGIN} -->\n"
        with self.assertRaisesRegex(ValueError, "malformed|out of order"):
            merge_generated(malformed, "body", "markdown")

    def test_nested_marker_is_rejected(self) -> None:
        nested = (
            f"<!-- {BEGIN} -->\n"
            f"<!-- {BEGIN} -->\ninner\n<!-- {END} -->\n"
            f"<!-- {END} -->\n"
        )
        with self.assertRaisesRegex(ValueError, "exactly one|Nested"):
            merge_generated(nested, "body", "markdown")

    def test_check_mode_detects_drift_without_writing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            path = Path(temp_name) / "artifact.md"
            path.write_text(compose_generated("old", "markdown"), encoding="utf-8")
            before = path.read_bytes()
            self.assertTrue(write_or_check(path, "new", "markdown", check=True))
            self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
