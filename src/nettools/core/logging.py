"""
Logging configuration for nettools.
"""

from __future__ import annotations

import logging
from pathlib import Path

from nettools.core.constants import LOG_FORMAT


def setup_logging(
    verbose: bool = False,
    log_file: Path | None = None,
) -> logging.Logger:
    """
    Configure application logging.

    Args:
        verbose: Enable debug logging.
        log_file: Optional file path for logs.

    Returns:
        Configured nettools logger.
    """

    logger = logging.getLogger("nettools")

    if logger.handlers:
        return logger

    level = logging.DEBUG if verbose else logging.INFO

    logger.setLevel(level)

    formatter = logging.Formatter(LOG_FORMAT)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


__all__ = ["setup_logging"]
