"""
Core application utilities.
"""

from __future__ import annotations

from portscout.core.config import Config, DEFAULT_CONFIG
from portscout.core.console import console
from portscout.core.logging import setup_logging

__all__ = [
    "Config",
    "DEFAULT_CONFIG",
    "console",
    "setup_logging",
]