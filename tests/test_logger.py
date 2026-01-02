# FILE: tests/test_logger.py


from pathlib import Path

import pytest

from datafun_toolkit.logger import get_logger, log_header


def test_get_logger_creates_log_file_in_project_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """REQ.TEST.LOGGER: get_logger writes log file at detected project root."""
    root: Path = tmp_path
    (root / "pyproject.toml").write_text('[project]\nname="x"\nversion="0.0.0"\n', encoding="utf-8")

    # Work from a nested directory to ensure root detection works via cwd
    nested: Path = root / "work" / "here"
    nested.mkdir(parents=True)
    monkeypatch.chdir(nested)

    log_name: str = "test-project.log"
    logger = get_logger("datafun-test", level="INFO", log_file_name=log_name)
    log_header(logger, "datafun-test")
    logger.info("hello")

    log_path: Path = root / log_name
    assert log_path.exists()

    text: str = log_path.read_text(encoding="utf-8")
    assert "=== RUN START ===" in text
    assert "project=datafun-test" in text
    assert "python=" in text
    assert "os=" in text
    assert "shell=" in text
    assert "cwd=" in text


def test_get_logger_does_not_add_duplicate_handlers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """REQ.TEST.LOGGER: repeated get_logger calls do not duplicate handlers."""
    root: Path = tmp_path
    (root / "pyproject.toml").write_text('[project]\nname="x"\nversion="0.0.0"\n', encoding="utf-8")
    nested: Path = root / "n"
    nested.mkdir()
    monkeypatch.chdir(nested)

    logger1 = get_logger("datafun-test-dup", level="INFO", log_file_name="dup.log")
    handlers_before: int = len(logger1.handlers)

    logger2 = get_logger("datafun-test-dup", level="INFO", log_file_name="dup.log")
    handlers_after: int = len(logger2.handlers)

    assert logger1 is logger2
    assert handlers_before == handlers_after
    # Expect exactly console + file in your implementation
    assert handlers_after == 2


def test_log_header_is_privacy_safe_relative_cwd(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """REQ.TEST.SANITIZE: header logs cwd as repo-relative when inside repo."""
    root: Path = tmp_path
    (root / "pyproject.toml").write_text('[project]\nname="x"\nversion="0.0.0"\n', encoding="utf-8")

    nested: Path = root / "a" / "b"
    nested.mkdir(parents=True)
    monkeypatch.chdir(nested)

    log_name: str = "header.log"
    logger = get_logger("datafun-header", level="INFO", log_file_name=log_name)
    log_header(logger, "datafun-header")

    log_path: Path = root / log_name
    text: str = log_path.read_text(encoding="utf-8")

    # We should see a repo-relative cwd like "a/b" (platform separators vary)
    assert "cwd=" in text
    assert "cwd=a" in text or "cwd=a\\" in text or "cwd=a/" in text
