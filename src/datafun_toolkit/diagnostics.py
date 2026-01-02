"""
diagnostics.py - Diagnostic environment detection functions.

Provides privacy-safe helpers for gathering environment information
for logging and debugging purposes.

OBS.EXECUTE:
  Open a terminal in the root project directory and run:
  uv run src/datafun_toolkit/diagnostics.py

REQ: Open each Python module (file) with a three-quoted docstring.
REQ: Open each public function with a three-quoted docstring.
WHY: Provide context for maintainers and users.
"""

# REQ: Imports first, use ruff to "Organize Imports".
import os
from pathlib import Path
import platform

# REQ: List the public functions provided by this module.
__all__ = ["detect_shell", "detect_os", "detect_python"]


def detect_shell() -> str:
    """Attempt to identify user shell / terminal in a privacy-safe way.

    REQ.DIAGNOSTICS:
      - Do not log usernames, hostnames, or full paths
      - Use environment variables only (no subprocess calls)

    WHY.DIAGNOSTICS:
      - Shell differences explain many command and path issues
      - Helps instructors debug pasted logs quickly

    OBS.DIAGNOSTICS:
      - Heuristic only; may return "unknown"
      - Different terminals expose different environment variables
    """
    env = os.environ

    # PowerShell (Windows)
    if env.get("PSModulePath"):
        # Distinguish pwsh vs Windows PowerShell when possible
        comspec = env.get("ComSpec", "").lower()
        if "pwsh" in comspec:
            return "pwsh"
        return "powershell"

    # Unix-like shells (macOS/Linux, Git Bash)
    shell = env.get("SHELL")
    if shell:
        return Path(shell).name

    # Fallback: terminal type (less precise, but useful)
    term = env.get("TERM")
    if term:
        return term

    return "unknown"


def detect_os() -> str:
    """Return a concise operating system description.

    OBS:
      - Uses coarse-grained OS info only
      - Safe to log publicly
    """
    return f"{platform.system()} {platform.release()}"


def detect_python() -> str:
    """Return the active Python version string."""
    return platform.python_version()


def main() -> None:
    """REQ: Example usage showing function calls and output."""
    # Call each function and assign to a local variable
    shell: str = detect_shell()
    os_info: str = detect_os()
    python_version: str = detect_python()

    # Use formatted strings (f-strings) to print the results
    print(f"Shell:  {shell}")
    print(f"OS:     {os_info}")
    print(f"Python: {python_version}")


if __name__ == "__main__":
    # REQ: If module is run as a script, call main() to demonstrate usage.
    main()
