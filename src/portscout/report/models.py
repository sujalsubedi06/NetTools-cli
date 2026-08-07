"""
Report data models.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class SecurityReport:
    """
    Generated security report.
    """

    target: str
    sections: dict[str, Any]