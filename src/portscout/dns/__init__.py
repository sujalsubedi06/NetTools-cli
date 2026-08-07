"""
DNS discovery package.
"""

from __future__ import annotations

from portscout.dns.models import DNSRecord
from portscout.dns.resolver import DNSResolver

__all__ = [
    "DNSRecord",
    "DNSResolver",
]
