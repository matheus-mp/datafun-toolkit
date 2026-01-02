# Examples

Typical usage patterns for the DataFun Toolkit.

These examples assume the package is installed and imported.

## Example: Logging a Run Header

    from datafun_toolkit.logger import get_logger, log_header

    logger = get_logger("datafun-project", level="INFO")
    log_header(logger, "datafun-project")

    logger.info("Starting analysis...")

Example output (sanitized):

    === RUN START ===
    project=datafun-project
    repo_dir=datafun-project
    python=3.12.1
    os=Windows 11
    shell=pwsh
    cwd=src
    github_actions=False

## Example: Safe Path Logging

    from pathlib import Path
    from datafun_toolkit.paths import find_project_root, safe_relpath_str

    root = find_project_root()
    print(f"Working directory: {safe_relpath_str(Path.cwd(), root)}")

## Example: Environment Diagnostics

    from datafun_toolkit.diagnostics import detect_shell, detect_os, detect_python

    print(detect_shell())
    print(detect_os())
    print(detect_python())

OBS:
- This information is safe to paste into issue reports or grading feedback.

## When to Use This Toolkit

Use it when you want:
- predictable logging output
- CI-safe diagnostics
- consistent behavior across student machines

Do not use it for:
- performance benchmarking
- security auditing
- deep system inspection
