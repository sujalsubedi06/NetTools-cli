"""
TCP scanning package.
"""

from __future__ import annotations

from nettools.scanner.engine import TCPScanner
from nettools.scanner.models import PortResult
from nettools.scanner.services import get_service_name
from nettools.scanner.utils import (
    get_common_ports,
    parse_port_range,
    validate_port,
)
from nettools.scanner.validator import resolve_target

__all__ = [
    "TCPScanner",
    "PortResult",
    "get_service_name",
    "get_common_ports",
    "parse_port_range",
    "validate_port",
    "resolve_target",
]
