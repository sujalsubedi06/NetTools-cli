"""
Application constants.
"""

from __future__ import annotations

DEFAULT_TIMEOUT: float = 3.0
DEFAULT_WORKERS: int = 50
DEFAULT_OUTPUT_FORMAT: str = "terminal"

LOG_FORMAT: str = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)

APP_NAME: str = "PortScout"

__all__ = [
    "DEFAULT_TIMEOUT",
    "DEFAULT_WORKERS",
    "DEFAULT_OUTPUT_FORMAT",
    "LOG_FORMAT",
    "APP_NAME",
]