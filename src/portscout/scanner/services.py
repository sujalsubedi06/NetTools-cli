"""
Common TCP service mappings.
"""

from __future__ import annotations


COMMON_SERVICES: dict[int, str] = {
    20: "ftp-data",
    21: "ftp",
    22: "ssh",
    23: "telnet",
    25: "smtp",
    53: "dns",
    80: "http",
    110: "pop3",
    143: "imap",
    443: "https",
    3306: "mysql",
    5432: "postgresql",
    6379: "redis",
    8080: "http-proxy",
}


def get_service_name(port: int) -> str:
    """
    Return a known service name for a port.

    Args:
        port: TCP port number.

    Returns:
        Service name or unknown.
    """

    return COMMON_SERVICES.get(port, "unknown")


__all__ = [
    "COMMON_SERVICES",
    "get_service_name",
]