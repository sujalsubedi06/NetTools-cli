"""
Output formatting utilities.
"""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any


def serialize(data: Any) -> Any:
    """
    Convert objects into JSON-compatible data.
    """

    if is_dataclass(data):
        return asdict(data)

    if isinstance(data, list):
        return [
            serialize(item)
            for item in data
        ]

    if isinstance(data, dict):
        return {
            key: serialize(value)
            for key, value in data.items()
        }

    if isinstance(data, Path):
        return str(data)

    return data


def to_json(data: Any) -> str:
    """
    Convert data into formatted JSON.
    """

    return json.dumps(
        serialize(data),
        indent=4,
        default=str,
    )


def write_json(
    data: Any,
    output: str | Path,
) -> None:
    """
    Write JSON data to file.
    """

    path = Path(output)

    path.write_text(
        to_json(data),
        encoding="utf-8",
    )