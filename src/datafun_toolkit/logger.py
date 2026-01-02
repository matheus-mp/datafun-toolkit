"""
logger.py — Logging utilities for DataFun projects.

Provides a standardized logger setup and a privacy-safe run header.

OBS.EXECUTE:
  Open a terminal in the root project directory and run:
  uv run src/datafun_toolkit/logger.py

REQ: Open each Python module (file) with a three-quoted docstring.
REQ: Open each public function with a three-quoted docstring.
WHY: Provide context for maintainers and users.
"""

# REQ: Imports first, use ruff to "Organize Imports".
import logging
import os
from pathlib import Path

from .diagnostics import detect_os, detect_python, detect_shell
from .paths import find_project_root, safe_relpath_str

__all__ = ["get_logger", "log_header"]


def get_logger(
    project_name: str,
    *,
    level: str = "INFO",
    log_file_name: str = "project.log",
) -> logging.Logger:
    """Return a configured logger for the project.

    REQ.LOGGING:
      - Provide standard logging methods: debug/info/warning/error
      - Write logs to both console and file
      - Avoid duplicate handlers on repeated calls

    WHY.LOGGING:
      - Make execution visible
      - Support debugging and grading

    OBS.LOGGING:
      - Uses Python stdlib logging (industry standard)
      - Log file is created at the project root
    """
    root: Path = find_project_root()
    log_file: Path = root / log_file_name
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Map level string to stdlib logging int level
    level_int: int = getattr(logging, level.upper(), logging.INFO)

    logger: logging.Logger = logging.getLogger(project_name)
    _configure_handlers(logger, log_file=log_file, level=level_int)
    return logger


def log_header(logger: logging.Logger, project_name: str) -> None:
    """Log a standardized, privacy-safe run header.

    REQ.SANITIZE:
      - Do not log usernames, hostnames, or full paths

    WHY.SANITIZE:
      - Enable debugging without exposing personal information

    OBS.HEADER:
      - Header appears once per run
      - Same output locally and in GitHub Actions
    """
    root: Path = find_project_root()

    logger.info("=== RUN START ===")
    logger.info(f"project={project_name}")
    logger.info(f"repo_dir={root.name}")
    logger.info(f"python={detect_python()}")
    logger.info(f"os={detect_os()}")
    logger.info(f"shell={detect_shell()}")
    logger.info(f"cwd={safe_relpath_str(Path.cwd(), root)}")
    logger.info(f"github_actions={bool(os.getenv('GITHUB_ACTIONS'))}")


def _configure_handlers(logger: logging.Logger, log_file: Path, level: int) -> None:
    """Configure console + file handlers once.

    REQ.LOGGING:
      - Do not add duplicate handlers
      - Use consistent formatting across console and file
    """
    logger.setLevel(level)
    logger.propagate = False

    # OBS: Avoid duplicate handlers if called multiple times
    if logger.handlers:
        return

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)


def main() -> None:
    """REQ: Example usage showing function calls and output."""
    logger: logging.Logger = get_logger("datafun-example", level="DEBUG")
    log_header(logger, "datafun-example")
    logger.info("This is an info message.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")


if __name__ == "__main__":
    main()
