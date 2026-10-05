from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "scaffold_project.py"
SPEC = importlib.util.spec_from_file_location("scaffold_project", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class ScaffoldProjectTests(unittest.TestCase):
    def test_alias_resolution(self) -> None:
        self.assertEqual(MODULE.resolve_template("django"), "django_drf")
        self.assertEqual(MODULE.resolve_template("data"), "data_engineer")
        self.assertEqual(MODULE.resolve_template("django rest framework"), "django_drf")

    def test_generate_data_engineer_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir)
            MODULE.scaffold_project("data_engineer", output)

            self.assertTrue((output / "pyproject.toml").exists())
            self.assertTrue((output / "CHANGELOG.md").exists())
            self.assertTrue((output / "pipelines/jobs/example_job.py").exists())

    def test_non_empty_output_requires_force(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir)
            (output / "existing.txt").write_text("keep", encoding="utf-8")

            with self.assertRaises(FileExistsError):
                MODULE.scaffold_project("fastapi", output)


if __name__ == "__main__":
    unittest.main()
