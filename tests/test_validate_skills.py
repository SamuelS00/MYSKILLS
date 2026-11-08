"""Behavior checks for skill discovery and common manifest errors."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from validate_skills import validate


class ValidatorTests(unittest.TestCase):
    def test_valid_skill(self):
        with TemporaryDirectory() as temporary:
            skill = Path(temporary) / "example-skill"
            skill.mkdir()
            (skill / "SKILL.md").write_text("---\nname: example-skill\ndescription: Use for examples.\n---\n\n# Steps\nDo the work.\n")
            self.assertEqual(validate(Path(temporary)), [])

    def test_missing_manifest(self):
        with TemporaryDirectory() as temporary:
            (Path(temporary) / "missing").mkdir()
            self.assertTrue(any("missing SKILL.md" in error for error in validate(Path(temporary))))

    def test_invalid_frontmatter_and_name(self):
        with TemporaryDirectory() as temporary:
            skill = Path(temporary) / "Bad_Name"
            skill.mkdir()
            (skill / "SKILL.md").write_text("name: other\n")
            errors = validate(Path(temporary))
            self.assertTrue(any("frontmatter" in error for error in errors))

    def test_missing_description(self):
        with TemporaryDirectory() as temporary:
            skill = Path(temporary) / "example"
            skill.mkdir()
            (skill / "SKILL.md").write_text("---\nname: example\n---\nDo it.\n")
            self.assertTrue(any("description" in error for error in validate(Path(temporary))))


if __name__ == "__main__":
    unittest.main()
