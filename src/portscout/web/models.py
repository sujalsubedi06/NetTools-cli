"""
Web information data models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WebInfo:
    """
    Web response information.
    """

    url: str
    status_code: int
    response_time: float
    server: str | None
    content_type: str | None
    title: str | None
    https: bool
    redirects: int
    security_headers: dict[str, str]
