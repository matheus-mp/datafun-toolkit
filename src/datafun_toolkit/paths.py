"""paths.py - Path utilities for DataFun projects.

Provides functions to find project roots and sanitize paths.

OBS.EXECUTE:
  Open a terminal in the root project directory and run:
  uv run src/datafun_toolkit/paths.py

REQ: Open each Python module (file) with a three-quoted docstring.
REQ: Open each public function with a three-quoted docstring.
WHY: Provide context for maintainers and users.
"""

from pathlib import Path

__all__ = ["find_project_root", "safe_relpath_str"]


def find_project_root(start: Path | None = None) -> Path:
    """Return the project root directory.

    Arguments:
      start: Optional starting directory (defaults to cwd)

    Returns:
      The project root directory as a pathlib.Path object.

    REQ.PATHS:
      - Identify the nearest ancestor containing pyproject.toml or .git
      - Work regardless of current working directory

    WHY.PATHS:
      - Prevent hard-coded paths
      - Ensure code runs the same locally and in CI

    OBS.PATHS:
      - Falls back to the starting directory if no markers are found
      - Cross-platform (Windows/macOS/Linux)
    """
    here = (start or Path.cwd()).resolve()
    for p in (here, *here.parents):
        if (p / "pyproject.toml").exists() or (p / ".git").exists():
            return p
    return here


def safe_relpath_str(path: Path, root: Path) -> str:
    """Return a sanitized, repo-relative string of the path when possible.

    Arguments:
      path: The path to sanitize.
      root: The project root directory to which the path should be made relative.

    Returns:
      A string representing the path relative to the project root,
      or the basename if the path is outside the project root.

    REQ.SANITIZE:
      - Do not emit full user home paths
      - Prefer repo-relative paths for logs and messages

    OBS.SANITIZE:
      - Falls back to basename if path is outside the project root
    """
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except (ValueError, OSError):
        return path.name


def main() -> None:
    """REQ: Example usage showing function calls and output."""
    project_root: Path = find_project_root()

    # OBS: Demonstrate sanitization using a path we always have.
    # This avoids hard-coded paths that may not exist on all machines.
    current_dir: Path = Path.cwd()
    relative_path: str = safe_relpath_str(current_dir, project_root)

    print(f"Project root: {project_root}")
    print(f"Sanitized relative path: {relative_path}")


if __name__ == "__main__":
    # REQ: If module is run as a script, call main() to demonstrate usage.
    main()
