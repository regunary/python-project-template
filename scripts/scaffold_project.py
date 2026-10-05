from __future__ import annotations

import argparse
import shutil
from pathlib import Path

TEMPLATE_ALIASES = {
    "django": "django_drf",
    "django_drf": "django_drf",
    "django_rest_framework": "django_drf",
    "django_and_drf": "django_drf",
    "drf": "django_drf",
    "flask": "flask",
    "fastapi": "fastapi",
    "data": "data_engineer",
    "data_engineer": "data_engineer",
    "ai": "ai",
}


def templates_root() -> Path:
    return Path(__file__).resolve().parents[1] / "scaffolds"


def resolve_template(value: str) -> str:
    key = value.strip().lower().replace("-", "_").replace("+", "_")
    key = key.replace(" ", "_")
    key = key.replace("__", "_")
    if key not in TEMPLATE_ALIASES:
        supported = ", ".join(sorted(set(TEMPLATE_ALIASES.values())))
        raise ValueError(f"Unknown template '{value}'. Supported templates: {supported}")
    return TEMPLATE_ALIASES[key]


def scaffold_project(template: str, output: Path, force: bool = False) -> Path:
    selected = resolve_template(template)
    source = templates_root() / selected
    if not source.exists():
        raise FileNotFoundError(f"Template folder is missing: {source}")

    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)

    if any(output.iterdir()) and not force:
        raise FileExistsError(
            f"Output directory '{output}' is not empty. Use --force to overwrite files."
        )

    for entry in source.iterdir():
        target = output / entry.name
        if entry.is_dir():
            shutil.copytree(entry, target, dirs_exist_ok=force)
        else:
            if target.exists() and not force:
                raise FileExistsError(
                    f"Target file '{target}' already exists. Use --force to overwrite files."
                )
            shutil.copy2(entry, target)

    return output


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a root project structure from a selected template skill."
    )
    parser.add_argument(
        "--template",
        required=True,
        help="Template name: django_drf, flask, fastapi, data_engineer, ai",
    )
    parser.add_argument(
        "--output",
        default=".",
        help="Output directory for the generated project root",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files in the output directory",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    output = scaffold_project(args.template, Path(args.output), force=args.force)
    print(f"Scaffolded '{resolve_template(args.template)}' template into {output}")


if __name__ == "__main__":
    main()
