"""
DNS CLI command.
"""

from __future__ import annotations

import time

import typer
from rich.panel import Panel
from rich.table import Table

from portscout.core.console import console
from portscout.core.output import to_json
from portscout.dns import DNSResolver
from portscout.utils.validators import validate_domain


def dns(
    domain: str = typer.Argument(
        ...,
        help="Domain name to query.",
    ),
    reverse: str | None = typer.Option(
        None,
        "--reverse",
        "-r",
        help="Perform reverse lookup for an IP address.",
    ),
    json_output: bool = typer.Option(
        False,
        "--json",
        help="Output results as JSON.",
    ),
) -> None:
    """
    Lookup DNS records for a domain.
    """

    resolver = DNSResolver()

    if reverse is None and not validate_domain(domain):
        console.print(
            "[red]Invalid domain format.[/red]"
        )
        raise typer.Exit(code=1)

    if reverse:
        hostname = resolver.reverse_lookup(reverse)

        if json_output:
            console.print(
                to_json(
                    {
                        "ip": reverse,
                        "hostname": hostname,
                    }
                )
            )
            raise typer.Exit()

        if hostname:
            console.print(
                Panel(
                    f"[cyan]{reverse}[/cyan]\n\n"
                    f"Hostname: [green]{hostname}[/green]",
                    title="Reverse DNS Lookup",
                    border_style="cyan",
                )
            )
        else:
            console.print(
                Panel(
                    "No reverse DNS record found.",
                    title="Reverse DNS Lookup",
                    border_style="yellow",
                )
            )

        return

    start = time.perf_counter()

    console.print(
        f"[cyan]Querying DNS records for[/cyan] {domain}"
    )

    records = resolver.lookup_all(domain)

    duration = time.perf_counter() - start

    if not records:
        console.print(
            Panel(
                f"No DNS records found for {domain}",
                title="DNS Error",
                border_style="red",
            )
        )
        raise typer.Exit(code=1)

    if json_output:
        console.print(
            to_json(records)
        )
        raise typer.Exit()

    console.print(
        Panel(
            f"""
Domain: {domain}
Records Found: {len(records)}
Query Time: {duration:.3f}s
            """.strip(),
            title="DNS Summary",
            border_style="cyan",
        )
    )

    table = Table(
        title=f"DNS Records: {domain}",
    )

    table.add_column(
        "TYPE",
        style="cyan",
    )

    table.add_column(
        "VALUE",
    )

    table.add_column(
        "TTL",
        justify="right",
    )

    for record in records:
        value = record.value

        if record.record_type == "TXT":
            value = value[:80]

        table.add_row(
            record.record_type,
            value,
            (
                str(record.ttl)
                if record.ttl
                else "-"
            ),
        )

    console.print(table)