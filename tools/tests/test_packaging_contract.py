"""Regression tests for release packaging boundaries."""

from __future__ import annotations

import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class PackagingContractTests(unittest.TestCase):
    def git_ignores(self, relative_path: str) -> bool:
        result = subprocess.run(
            ["git", "check-ignore", "--quiet", "--", relative_path],
            cwd=ROOT,
            check=False,
        )
        self.assertIn(result.returncode, (0, 1))
        return result.returncode == 0

    def test_authored_documentation_sources_are_not_ignored(self) -> None:
        sources = sorted((ROOT / "docs" / "site").rglob("*.md"))
        self.assertEqual(19, len(sources))
        for source in sources:
            relative = source.relative_to(ROOT).as_posix()
            self.assertFalse(self.git_ignores(relative), relative)

    def test_generated_site_directories_are_ignored_at_repository_root(self) -> None:
        self.assertTrue(self.git_ignores("site/index.html"))
        self.assertTrue(self.git_ignores(".site-docs/index.md"))


if __name__ == "__main__":
    unittest.main()
