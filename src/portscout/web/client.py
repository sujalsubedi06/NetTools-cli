"""
HTTP information gathering client.
"""

from __future__ import annotations

import time

import requests

from portscout.web.models import WebInfo


class WebClient:
    """
    Collects web server information.
    """

    SECURITY_HEADERS = (
        "strict-transport-security",
        "content-security-policy",
        "x-frame-options",
        "x-content-type-options",
        "referrer-policy",
    )

    def __init__(
        self,
        timeout: float = 5.0,
    ) -> None:
        self.timeout = timeout

    def fetch(
        self,
        url: str,
    ) -> WebInfo | None:
        if not url.startswith(
            ("http://", "https://")
        ):
            url = f"https://{url}"

        start = time.perf_counter()

        try:
            response = requests.get(
                url,
                timeout=self.timeout,
                allow_redirects=True,
                headers={
                    "User-Agent": "PortScout/1.0"
                },
            )
        except Exception:
            return None

        duration = time.perf_counter() - start

        headers = {
            key.lower(): value
            for key, value in response.headers.items()
        }

        security_headers = {
            header: headers[header]
            for header in self.SECURITY_HEADERS
            if header in headers
        }

        return WebInfo(
            url=str(response.url),
            status_code=response.status_code,
            response_time=duration,
            server=headers.get("server"),
            content_type=headers.get("content-type"),
            title=self._extract_title(response.text),
            https=response.url.startswith("https://"),
            redirects=len(response.history),
            security_headers=security_headers,
        )

    def _extract_title(
        self,
        html: str,
    ) -> str | None:
        lower = html.lower()

        start = lower.find("<title>")
        end = lower.find("</title>")

        if start == -1 or end == -1:
            return None

        return html[start + 7:end].strip()
