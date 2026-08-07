"""
Application configuration management.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from nettools.core.constants import (
    DEFAULT_OUTPUT_FORMAT,
    DEFAULT_TIMEOUT,
    DEFAULT_WORKERS,
)


@dataclass(frozen=True, slots=True)
class Config:
    """
    Global nettools configuration.

    Attributes:
        timeout: Network operation timeout in seconds.
        workers: Number of concurrent workers.
        output_format: Default export/output format.
        log_file: Optional log file path.
        verbose: Enable verbose logging.
    """

    timeout: float = DEFAULT_TIMEOUT
    workers: int = DEFAULT_WORKERS
    output_format: str = DEFAULT_OUTPUT_FORMAT
    log_file: Path | None = None
    verbose: bool = False


DEFAULT_CONFIG = Config()

__all__ = [
    "Config",
    "DEFAULT_CONFIG",
]
