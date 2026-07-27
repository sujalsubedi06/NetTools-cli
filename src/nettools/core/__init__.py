"""
Core application utilities.
"""

from __future__ import annotations

from nettools.core.config import Config, DEFAULT_CONFIG
from nettools.core.console import console
from nettools.core.logging import setup_logging

__all__ = [
    "Config",
    "DEFAULT_CONFIG",
    "console",
    "setup_logging",
]
