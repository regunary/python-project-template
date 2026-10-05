# python-project-template

A lightweight Python template designed for teams using agent skills across backend, data engineering, and AI workflows.

## Included app templates

- `templates/django_drf/`: starter layout for Django + Django REST Framework
- `templates/flask/`: starter layout for Flask APIs
- `templates/fastapi/`: starter layout for FastAPI services

## Included skill profiles

- `profiles/backend/`: backend service checklist
- `profiles/data_engineer/`: data pipeline checklist
- `profiles/ai/`: AI service checklist

## Versioning and changelog workflow

This template uses **Commitizen** to keep versions and changelog updates simple.

### Bump version + update changelog

```bash
pip install -e .[dev]
cz bump
```

`cz bump` updates:

- version in `pyproject.toml`
- `CHANGELOG.md`

## Quick start

```bash
# for Django + DRF starter dependencies
pip install -e .[django]

# for Flask starter dependencies
pip install -e .[flask]

# for FastAPI starter dependencies
pip install -e .[fastapi]
```
