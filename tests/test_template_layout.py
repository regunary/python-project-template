from pathlib import Path
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TemplateLayoutTests(unittest.TestCase):
    def test_framework_templates_exist(self) -> None:
        expected = [
            ROOT / "templates/django_drf/manage.py",
            ROOT / "templates/flask/app/__init__.py",
            ROOT / "templates/fastapi/app/main.py",
        ]
        for path in expected:
            self.assertTrue(path.exists(), f"Missing template file: {path}")

    def test_commitizen_is_configured(self) -> None:
        pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        commitizen = pyproject["tool"]["commitizen"]

        self.assertEqual(commitizen["version"], pyproject["project"]["version"])
        self.assertEqual(commitizen["changelog_file"], "CHANGELOG.md")


if __name__ == "__main__":
    unittest.main()
