"""
Subdomain data models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SubdomainResult:
    """
    Represents a discovered subdomain.
    """

    subdomain: str
    resolved: bool
    address: str | None = None
