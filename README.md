# python-project-template

A Python project template that can generate a **single-purpose project root** for the stack/skill you ask for.

## Why this structure

When you tell Codex/Claude to use a specific stack (for example Django + DRF) or a specific skill (for example data engineer), you should get a root folder that only contains what that project type needs.

This repository now provides that through ready-to-copy root scaffolds and a small scaffold CLI.

## Available scaffold types

- `django_drf` (aliases: `django`, `drf`)
- `flask`
- `fastapi`
- `data_engineer` (alias: `data`)
- `ai`

## Generate a project root for one skill/template

```bash
python scripts/scaffold_project.py --template django_drf --output /path/to/new-project
python scripts/scaffold_project.py --template data_engineer --output /path/to/new-project
python scripts/scaffold_project.py --template ai --output /path/to/new-project
```

If output is not empty, pass `--force` to overwrite.

## Scaffold contents

Each generated project root includes:

- stack/skill-specific source layout
- `pyproject.toml` with only relevant dependencies
- `CHANGELOG.md` starter

Scaffold sources are stored under `scaffolds/`.

## Versioning and changelog in this template repository

This repository uses **Commitizen** to keep template versioning/changelog updates simple.

```bash
pip install -e .[dev]
cz bump
```

`cz bump` updates:

- version in `pyproject.toml`
- `CHANGELOG.md`
