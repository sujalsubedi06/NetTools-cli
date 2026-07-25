"""
Subdomain enumeration CLI commands.
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from portscout.core.output import (
    to_json,
    write_json,
)
from portscout.subdomains import SubdomainEnumerator


console = Console()


def subdomains(
    domain: str,
    wordlist: Path | None = typer.Option(
        None,
        "--wordlist",
        "-w",
        help="Custom subdomain wordlist.",
    ),
    json_output: bool = typer.Option(
        False,
        "--json",
        help="Output results as JSON.",
    ),
    output: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Save results as JSON file.",
    ),
) -> None:
    """
    Enumerate subdomains for a domain.
    """

    console.print(
        f"[bold blue]Enumerating subdomains for[/bold blue] {domain}"
    )

    enumerator = SubdomainEnumerator(
        wordlist=wordlist,
    )

    results = enumerator.enumerate(
        domain,
    )

    if output:
        saved_path = write_json(
            results,
            output,
        )

        console.print(
            f"[green]Saved JSON output:[/green] {saved_path}"
        )

    if json_output:
        console.print(
            to_json(results)
        )
        raise typer.Exit()

    if not results:
        console.print(
            "[yellow]No subdomains found.[/yellow]"
        )
        return

    table = Table(
        title=f"Subdomains: {domain}",
    )

    table.add_column(
        "SUBDOMAIN",
        style="cyan",
    )

    table.add_column(
        "ADDRESS",
        style="green",
    )

    for result in results:
        table.add_row(
            result.subdomain,
            result.address or "-",
        )

    console.print(table)

    console.print(
        f"\n[bold green]Found:[/bold green] {len(results)}"
    )