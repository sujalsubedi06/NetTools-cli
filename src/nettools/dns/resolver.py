"""
DNS resolver service.
"""

from __future__ import annotations

import socket

import dns.exception
import dns.resolver

from nettools.dns.models import DNSRecord


class DNSResolver:
    """
    DNS lookup service.
    """

    def __init__(
        self,
        timeout: float = 3.0,
    ) -> None:
        """
        Initialize resolver.
        """

        self.timeout = timeout

    def lookup(
        self,
        domain: str,
        record_type: str,
    ) -> list[DNSRecord]:
        """
        Query DNS records.
        """

        records: list[DNSRecord] = []

        try:
            answers = dns.resolver.resolve(
                domain,
                record_type,
                lifetime=self.timeout,
            )

            for answer in answers:
                records.append(
                    DNSRecord(
                        record_type=record_type,
                        value=str(answer),
                        ttl=(answers.rrset.ttl if answers.rrset else None),
                    )
                )

        except (
            dns.exception.DNSException,
            TimeoutError,
            Exception,
        ):
            return []

        return records

    def lookup_all(
        self,
        domain: str,
    ) -> list[DNSRecord]:
        """
        Lookup supported DNS records.
        """

        records: list[DNSRecord] = []

        for record_type in (
            "A",
            "AAAA",
            "MX",
            "TXT",
            "NS",
            "CNAME",
        ):
            records.extend(
                self.lookup(
                    domain,
                    record_type,
                )
            )

        return records

    def lookup_basic(
        self,
        domain: str,
    ) -> list[DNSRecord]:
        """
        Lookup A and AAAA records.
        """

        records: list[DNSRecord] = []

        for record_type in (
            "A",
            "AAAA",
        ):
            records.extend(
                self.lookup(
                    domain,
                    record_type,
                )
            )

        return records

    def reverse_lookup(
        self,
        address: str,
    ) -> str | None:
        """
        Perform reverse DNS lookup.
        """

        try:
            hostname, _, _ = socket.gethostbyaddr(
                address,
            )

            return hostname

        except (
            socket.herror,
            OSError,
            Exception,
        ):
            return None


__all__ = [
    "DNSResolver",
]
