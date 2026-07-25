"""
Target validation utilities.
"""

from __future__ import annotations

import socket
from ipaddress import ip_address


def resolve_target(target: str) -> str:
    """
    Resolve hostname or validate IP address.

    Args:
        target: Hostname or IP address.

    Returns:
        Resolved IPv4 address.

    Raises:
        ValueError: If target cannot be resolved.
    """

    try:
        ip_address(target)
        return target

    except ValueError:
        pass

    try:
        return socket.gethostbyname(target)

    except socket.gaierror as exc:
        raise ValueError(
            f"Unable to resolve target: {target}"
        ) from exc


__all__ = [
    "resolve_target",
]