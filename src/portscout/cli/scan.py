"""
Scan CLI command.
"""

from __future__ import annotations

import time

import typer
from rich.table import Table

from portscout.core.console import console
from portscout.scanner import (
    TCPScanner,
    get_common_ports,
    parse_port_range,
    resolve_target,
)


def scan(
    target: str = typer.Argument(
        ...,
        help="Target hostname or IP address.",
    ),
    ports: str | None = typer.Option(
        None,
        "--ports",
        "-p",
        help="Ports to scan. Examples: 80,443 or 20-25.",
    ),
    timeout: float = typer.Option(
        3.0,
        "--timeout",
        "-t",
        help="Connection timeout in seconds.",
    ),
    workers: int = typer.Option(
        50,
        "--workers",
        "-w",
        help="Number of concurrent workers.",
    ),
) -> None:
    """
    Scan TCP ports on a host.
    """

    try:
        selected_ports = (
            parse_port_range(ports)
            if ports
            else get_common_ports()
        )

    except ValueError as exc:
        console.print(
            f"[red]Invalid ports:[/red] {exc}"
        )
        raise typer.Exit(code=1) from exc

    try:
        resolved_target = resolve_target(target)

    except ValueError as exc:
        console.print(
            f"[red]Target error:[/red] {exc}"
        )
        raise typer.Exit(code=1) from exc

    console.print(
        f"[cyan]Scanning[/cyan] {target} "
        f"[dim]({resolved_target})[/dim]"
    )

    scanner = TCPScanner(
        timeout=timeout,
        workers=workers,
    )

    start = time.perf_counter()

    try:
        results = scanner.scan(
            resolved_target,
            selected_ports,
        )

    except KeyboardInterrupt:
        console.print(
            "\n[yellow]Scan interrupted.[/yellow]"
        )
        raise typer.Exit(code=1)

    duration = time.perf_counter() - start

    table = Table(
        title=f"Port Scan Results: {target}",
    )

    table.add_column(
        "PORT",
        style="cyan",
    )

    table.add_column(
        "STATUS",
    )

    table.add_column(
        "SERVICE",
    )

    table.add_column(
        "TIME",
    )

    for result in results:
        status = (
            "[green]OPEN[/green]"
            if result.is_open
            else "[red]CLOSED[/red]"
        )

        table.add_row(
            str(result.port),
            status,
            result.service,
            f"{result.response_time:.3f}s",
        )

    console.print(table)

    open_ports = [
        result
        for result in results
        if result.is_open
    ]

    console.print(
        f"\n[green]Completed[/green] "
        f"in {duration:.2f}s"
    )

    console.print(
        f"[cyan]Open ports:[/cyan] "
        f"{len(open_ports)}/{len(results)}"
    )
