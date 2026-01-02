# Data Analytics Fundamentals: Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/license/MIT)
![Build Status](https://github.com/denisecase/datafun-toolkit/actions/workflows/ci.yml/badge.svg)
[![Check Links](https://github.com/denisecase/datafun-toolkit/actions/workflows/links.yml/badge.svg)](https://github.com/denisecase/datafun-toolkit/actions/workflows/links.yml)

> Privacy-safe diagnostics, paths, and logging helpers for analytics projects.

## What This Provides

- `find_project_root()` and `safe_relpath_str()` for robust, repo-relative paths
- `get_logger()` for consistent console and file logging (using a standard logging API)
- `log_header()` for a privacy-safe logging header (shows OS, shell, Python version, repo-relative cwd)

This toolkit is designed for reuse.
It works the same locally and in GitHub Actions.

## Install (Choose One)

```shell
uv add datafun-toolkit
```

```shell
pip install datafun-toolkit
```

## Example

```python
from datafun_toolkit import find_project_root, get_logger, log_header, safe_relpath_str
from pathlib import Path

def main() -> None:
    logger = get_logger("example")
    log_header(logger, "example")

    root = find_project_root()
    logger.info(f"project_root={root.name}")
    logger.info(f"cwd={safe_relpath_str(Path.cwd(), root)}")

if __name__ == "__main__":
    main()
```

## Developer Setup

Tools:

- git
- uv
- VS Code

One-time setup:

```shell
uv self update
uv python pin 3.12
uv sync --extra dev --extra docs --upgrade
```

Before starting work:

```shell
git pull
```

After working, run checks:

```shell
git add .
uv run ruff check .
uv run ruff format .
uv run deptry .
uv run pyright
uv run pytest
uv run bandit -c pyproject.toml -r src
uv run pre-commit run --all-files
git add .
```

Build and serve docs:

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

## Annotations

[ANNOTATIONS.md](./ANNOTATIONS.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
