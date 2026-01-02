# API Reference

This page documents the public API of the `datafun-toolkit` package.

Only the documented functions below are considered stable.

## datafun_toolkit.paths

Utilities for locating the project root and sanitizing paths.

### find_project_root(start: Path | None = None) -> Path

Return the project root directory.

The project root is identified as the nearest parent directory containing either:

- pyproject.toml, or
- a .git directory

WHY:
- Prevents hard-coded paths
- Works regardless of current working directory
- Behaves the same locally and in CI

Example:

    from datafun_toolkit.paths import find_project_root
    root = find_project_root()

### safe_relpath_str(path: Path, root: Path) -> str

Return a sanitized, repo-relative path string when possible.

If the path cannot be made relative to the project root, the function returns only the filename.

WHY:
- Avoids leaking full home directory paths in logs
- Keeps log output short and shareable

Example:

    from pathlib import Path
    from datafun_toolkit.paths import find_project_root, safe_relpath_str

    root = find_project_root()
    safe_path = safe_relpath_str(Path.cwd(), root)

## datafun_toolkit.diagnostics

Lightweight environment detection helpers.

### detect_shell() -> str

Attempt to identify the active shell or terminal in a privacy-safe way.

Possible return values include:
- pwsh
- powershell
- bash
- zsh
- unknown

OBS:
- This function uses environment-variable heuristics only.

### detect_os() -> str

Return a concise operating system description.

Example output:

    Windows 11
    Linux 6.6
    Darwin 23.1

### detect_python() -> str

Return the active Python version string.

## datafun_toolkit.logger

Standardized logging helpers.

### get_logger(project_name: str, *, level: str = "INFO") -> logging.Logger

Return a configured Python logger that:

- Logs to both console and file
- Avoids duplicate handlers
- Uses consistent formatting

OBS:
- The log file is created at the project root.

### log_header(logger: logging.Logger, project_name: str) -> None

Emit a standardized, privacy-safe run header.

The header includes:
- project name
- repository directory name
- python version
- operating system
- shell
- current working directory (sanitized)
- whether running in GitHub Actions

OBS:
- Intended to be called once per run.

## Marker Files

### py.typed

This package includes a py.typed marker file as defined by PEP 561.

WHY:
- Type checkers (Pyright, Mypy) only trust inline type hints in installed packages when this marker is present.

OBS:
- The file may be empty; comments are allowed.
