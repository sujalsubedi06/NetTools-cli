"""
DNS data models.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DNSRecord:
    """
    Represents a DNS record.

    Attributes:
        record_type: DNS record type.
        value: Record value.
        ttl: Time to live.
    """

    record_type: str
    value: str
    ttl: int | None


__all__ = [
    "DNSRecord",
]
