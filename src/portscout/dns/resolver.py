"""
DNS resolver service.
"""

from __future__ import annotations

import dns.exception
import dns.resolver

from portscout.dns.models import DNSRecord


class DNSResolver:
    """
    DNS lookup service.

    Provides authorized DNS information discovery.
    """

    def __init__(
        self,
        timeout: float = 3.0,
    ) -> None:
        """
        Initialize resolver.

        Args:
            timeout: DNS query timeout.
        """

        self.timeout = timeout

    def lookup(
        self,
        domain: str,
        record_type: str,
    ) -> list[DNSRecord]:
        """
        Query DNS records.

        Args:
            domain: Domain name.
            record_type: DNS record type.

        Returns:
            List of DNS records.
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
                        ttl=answers.rrset.ttl
                        if answers.rrset
                        else None,
                    )
                )

        except (
            dns.exception.DNSException,
            TimeoutError,
        ):
            return []

        return records

    def lookup_basic(
        self,
        domain: str,
    ) -> list[DNSRecord]:
        """
        Lookup common A and AAAA records.

        Args:
            domain: Domain name.

        Returns:
            DNS records.
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


__all__ = [
    "DNSResolver",
]
