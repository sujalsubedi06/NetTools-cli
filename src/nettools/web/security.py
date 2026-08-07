"""
Web security checks.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class SecurityReport:
    https: bool
    missing_headers: list[str]
    score: int


SECURITY_HEADERS = {
    "strict-transport-security": "HSTS",
    "content-security-policy": "CSP",
    "x-frame-options": "Clickjacking Protection",
    "x-content-type-options": "MIME Protection",
    "referrer-policy": "Referrer Policy",
}


def analyze_security(
    url: str,
    headers: dict[str, str],
) -> SecurityReport:
    """
    Analyze basic web security posture.
    """

    normalized = {key.lower(): value for key, value in headers.items()}

    missing = [name for key, name in SECURITY_HEADERS.items() if key not in normalized]

    score = 100 - (len(missing) * 15)

    if not url.startswith("https://"):
        score -= 30

    if score < 0:
        score = 0

    return SecurityReport(
        https=url.startswith("https://"),
        missing_headers=missing,
        score=score,
    )
