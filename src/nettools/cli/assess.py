"""
Unified assessment CLI command.
"""

from __future__ import annotations

import json
from pathlib import Path

import typer
from rich.panel import Panel

from nettools.core.console import console
from nettools.core.output import write_json
from nettools.dns import DNSResolver
from nettools.subdomains import SubdomainEnumerator
from nettools.web import WebClient, analyze_security


def assess(
    target: str = typer.Argument(
        ...,
        help="Target domain.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Save assessment JSON output.",
    ),
) -> None:
    """
    Run complete nettools assessment.
    """

    console.print(
        Panel(
            f"""
Target:
{target}

Running:
✓ DNS Analysis
✓ Subdomain Discovery
✓ Web Inspection
            """.strip(),
            title="nettools Assessment",
            border_style="cyan",
        )
    )

    result = {
        "target": target,
        "dns": [],
        "subdomains": [],
        "web": None,
        "security": None,
    }

    # DNS

    try:
        resolver = DNSResolver()

        records = resolver.lookup_all(
            target,
        )

        result["dns"] = records

    except Exception:
        result["dns"] = []

    # Subdomains

    try:
        enumerator = SubdomainEnumerator()

        domains = enumerator.enumerate(
            target,
        )

        result["subdomains"] = domains

    except Exception:
        result["subdomains"] = []

    # Web

    try:
        client = WebClient()

        web = client.fetch(
            target,
        )

        if web:
            result["web"] = web

            result["security"] = analyze_security(
                web.url,
                web.security_headers,
            )

    except Exception:
        result["web"] = None
        result["security"] = None

    if output:
        write_json(
            result,
            output,
        )

        console.print(f"\n[green]Saved:[/green] {output}")

    else:
        console.print(
            json.dumps(
                result,
                indent=4,
                default=str,
            )
        )
