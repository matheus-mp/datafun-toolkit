# FILE: tests/test_diagnostics.py

from __future__ import annotations

from pathlib import Path

from pytest import MonkeyPatch

from datafun_toolkit.diagnostics import detect_os, detect_python, detect_shell


def test_detect_python_returns_version_string() -> None:
    """REQ.TEST.DIAGNOSTICS: detect_python returns a non-empty version string."""
    v: str = detect_python()
    assert isinstance(v, str)
    assert len(v) > 0
    assert "." in v


def test_detect_os_returns_concise_string() -> None:
    """REQ.TEST.DIAGNOSTICS: detect_os returns a non-empty OS string."""
    s: str = detect_os()
    assert isinstance(s, str)
    assert len(s) > 0


def test_detect_shell_uses_shell_env_when_present(monkeypatch: MonkeyPatch) -> None:
    """REQ.TEST.DIAGNOSTICS: detect_shell prefers SHELL when present."""
    # Clear PowerShell indicators so we don't short-circuit on Windows.
    monkeypatch.delenv("PSModulePath", raising=False)
    monkeypatch.delenv("ComSpec", raising=False)
    monkeypatch.delenv("TERM", raising=False)

    monkeypatch.setenv("SHELL", str(Path("/bin/zsh")))
    shell: str = detect_shell()
    assert shell == "zsh"


def test_detect_shell_returns_unknown_when_no_hints(monkeypatch: MonkeyPatch) -> None:
    """REQ.TEST.DIAGNOSTICS: detect_shell returns 'unknown' when no hints exist."""
    # Remove all vars used by detect_shell
    for k in ("PSModulePath", "ComSpec", "SHELL", "TERM"):
        monkeypatch.delenv(k, raising=False)

    shell: str = detect_shell()
    assert shell == "unknown"
