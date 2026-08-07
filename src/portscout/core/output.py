"""
Output formatting helpers.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any


def to_json(
    data: Any,
) -> str:
    """
    Convert data to JSON.
    """

    if hasattr(data, "__dataclass_fields__"):
        data = asdict(data)

    elif isinstance(data, list):
        data = [
            asdict(item)
            if hasattr(item, "__dataclass_fields__")
            else item
            for item in data
        ]

    return json.dumps(
        data,
        indent=4,
        default=str,
    )