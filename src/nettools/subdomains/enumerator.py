"""
Subdomain enumeration service.
"""

from __future__ import annotations

import socket
from pathlib import Path

from nettools.subdomains.models import SubdomainResult


class SubdomainEnumerator:
    """
    Wordlist based subdomain enumerator.
    """

    def __init__(
        self,
        wordlist: Path | None = None,
        timeout: float = 3.0,
    ) -> None:
        """
        Initialize enumerator.
        """

        self.timeout = timeout

        if wordlist is None:
            wordlist = Path(__file__).parent.parent.joinpath(
                "assets",
                "wordlists",
                "default.txt",
            )

        self.wordlist = wordlist

    def load_wordlist(self) -> list[str]:
        """
        Load subdomain names.
        """

        if not self.wordlist.exists():
            return []

        entries = self.wordlist.read_text(
            encoding="utf-8",
        ).splitlines()

        return sorted({entry.strip() for entry in entries if entry.strip()})

    def resolve(
        self,
        hostname: str,
    ) -> str | None:
        """
        Resolve hostname to IPv4 address.
        """

        try:
            socket.setdefaulttimeout(
                self.timeout,
            )

            return socket.gethostbyname(
                hostname,
            )

        except Exception:
            return None

    def enumerate(
        self,
        domain: str,
    ) -> list[SubdomainResult]:
        """
        Enumerate subdomains.
        """

        results: list[SubdomainResult] = []

        for prefix in self.load_wordlist():
            hostname = f"{prefix}.{domain}"

            address = self.resolve(
                hostname,
            )

            if address:
                results.append(
                    SubdomainResult(
                        subdomain=hostname,
                        resolved=True,
                        address=address,
                    )
                )

        return sorted(
            results,
            key=lambda item: item.subdomain,
        )
