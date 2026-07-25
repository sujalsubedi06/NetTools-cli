"""
Scanner data models.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class PortResult:
    """
    Represents a scanned port result.

    Attributes:
        host: Target hostname or IP address.
        port: Port number.
        is_open: Whether the port accepted a connection.
        service: Detected service name.
        response_time: Connection time in seconds.
        scanned_at: Scan timestamp.
    """

    host: str
    port: int
    is_open: bool
    service: str
    response_time: float
    scanned_at: datetime


__all__ = [
    "PortResult",
]