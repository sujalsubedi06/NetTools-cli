"""
DNS discovery package.
"""

from __future__ import annotations

from nettools.dns.models import DNSRecord
from nettools.dns.resolver import DNSResolver

__all__ = [
    "DNSRecord",
    "DNSResolver",
]
