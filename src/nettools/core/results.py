"""
Result storage manager.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from nettools.core.output import write_json


BASE_RESULTS_DIR = Path("results")


def sanitize_name(name: str) -> str:
    """
    Make safe filename.
    """

    return name.replace("/", "_").replace(":", "_").replace(".", "_")


def save_result(
    category: str,
    target: str,
    data,
) -> Path:
    """
    Save command result automatically.
    """

    folder = BASE_RESULTS_DIR / category

    folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{sanitize_name(target)}_{timestamp}.json"

    output_file = folder / filename

    write_json(
        data,
        output_file,
    )

    return output_file
