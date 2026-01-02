"""tools/run_pytest.py - Script to run pytest with proper exit codes.

WHY: Ensure consistent test execution and exit codes for CI/CD pipelines.
"""

import subprocess
import sys


def main() -> int:
    """Run pytest and return appropriate exit codes.

    Run pytest normally.
    Exit code meanings:
       0 = all tests passed
       1 = tests failed
       2 = interrupted
       3 = internal error
       4 = usage error
       5 = no tests collected
    """
    result = subprocess.run([sys.executable, "-m", "pytest"], check=False)  # noqa: S603
    if result.returncode == 5:
        return 0
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
