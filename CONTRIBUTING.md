# Contributing

## Development setup

```bash
python -m pip install -e ".[dev]"
```

## Checks

Run these before opening a pull request:

```bash
python -m ruff check .
python -m pytest
python -m build
```

## Pull requests

- Keep changes scoped and explain the user-visible impact.
- Add or update tests when behavior changes.
- Prefer reusable low-level helpers in the package and keep form-specific flows in local runners.
