"""
datafun_toolkit - Core utilities for data analytics projects.

This package (datafun-toolkit) provides reusable, privacy-safe helpers for:
- project path discovery
- standardized logging
- diagnostic run headers

REQ.PACKAGE:
  - Expose a small, stable public API at the package level.

WHY.PACKAGE:
  - Enable simple imports
    (e.g., `from datafun_toolkit import get_logger`)
  - Hide internal module structure when appropriate.
"""

# REQ: Import public symbols from internal modules.
# WHY: Re-export selected helpers to define a clean package API.

from .logger import get_logger, log_header
from .paths import find_project_root

# REQ: Explicitly declare the public API of this package.
# WHY: Prevent accidental exposure of internal helpers.

__all__ = [
    "find_project_root",
    "get_logger",
    "log_header",
]
