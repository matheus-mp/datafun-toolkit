# FILE: tests/test_paths.py

from pathlib import Path

import pytest

from datafun_toolkit.paths import find_project_root, safe_relpath_str


def test_find_project_root_finds_pyproject(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """REQ.TEST.PATHS: find_project_root returns nearest ancestor with pyproject.toml."""
    root: Path = tmp_path
    (root / "pyproject.toml").write_text('[project]\nname="x"\nversion="0.0.0"\n', encoding="utf-8")

    nested: Path = root / "a" / "b" / "c"
    nested.mkdir(parents=True)

    # Start from nested and ensure we find the root containing pyproject.toml
    detected: Path = find_project_root(start=nested)
    assert detected == root


def test_safe_relpath_str_returns_repo_relative_or_basename(tmp_path: Path) -> None:
    """REQ.TEST.SANITIZE: safe_relpath_str returns a relative path when inside root, else basename."""
    root: Path = tmp_path
    inside: Path = root / "src" / "mod.py"
    inside.parent.mkdir(parents=True)
    inside.write_text("x=1\n", encoding="utf-8")

    outside: Path = tmp_path.parent / "outside.txt"

    rel_inside: str = safe_relpath_str(inside, root)
    assert rel_inside.replace("\\", "/") == "src/mod.py"

    rel_outside: str = safe_relpath_str(outside, root)
    assert rel_outside == outside.name
