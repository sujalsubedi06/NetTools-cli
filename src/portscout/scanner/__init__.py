"""
TCP scanning package.
"""

from __future__ import annotations

from portscout.scanner.engine import TCPScanner
from portscout.scanner.models import PortResult
from portscout.scanner.services import get_service_name

__all__ = [
    "TCPScanner",
    "PortResult",
    "get_service_name",
]