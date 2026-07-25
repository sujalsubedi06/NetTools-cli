"""
TCP scanning package.
"""

from __future__ import annotations

from portscout.scanner.engine import TCPScanner
from portscout.scanner.models import PortResult
from portscout.scanner.services import get_service_name
from portscout.scanner.utils import (
    get_common_ports,
    parse_port_range,
    validate_port,
)

__all__ = [
    "TCPScanner",
    "PortResult",
    "get_service_name",
    "get_common_ports",
    "parse_port_range",
    "validate_port",
]