"""
Scanner utility functions.
"""

from __future__ import annotations


COMMON_PORTS: list[int] = [
    20,
    21,
    22,
    23,
    25,
    53,
    80,
    110,
    143,
    443,
    3306,
    5432,
    6379,
    8080,
]


def validate_port(port: int) -> bool:
    """
    Validate a TCP port number.

    Args:
        port: Port number.

    Returns:
        True if valid, otherwise False.
    """

    return 1 <= port <= 65535


def parse_port_range(
    port_range: str,
) -> list[int]:
    """
    Parse a port range string.

    Supported formats:

    - "80"
    - "80,443"
    - "20-25"
    - "20-25,80,443"

    Args:
        port_range: User supplied port range.

    Returns:
        Sorted unique port numbers.
    """

    ports: set[int] = set()

    parts = port_range.split(",")

    for part in parts:
        value = part.strip()

        if "-" in value:
            start, end = value.split("-", maxsplit=1)

            start_port = int(start)
            end_port = int(end)

            if (
                not validate_port(start_port)
                or not validate_port(end_port)
                or start_port > end_port
            ):
                raise ValueError(
                    f"Invalid port range: {value}"
                )

            ports.update(
                range(
                    start_port,
                    end_port + 1,
                )
            )

        else:
            port = int(value)

            if not validate_port(port):
                raise ValueError(
                    f"Invalid port: {port}"
                )

            ports.add(port)

    return sorted(ports)


def get_common_ports() -> list[int]:
    """
    Return default common ports.

    Returns:
        List of common TCP ports.
    """

    return COMMON_PORTS.copy()


__all__ = [
    "COMMON_PORTS",
    "validate_port",
    "parse_port_range",
    "get_common_ports",
]