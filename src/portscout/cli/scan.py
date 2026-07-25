"""
Scan CLI command.
"""

from __future__ import annotations

import time

import typer
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
)
from rich.table import Table

from portscout.core.console import console
from portscout.core.output import to_json, write_json
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
    json_output: bool = typer.Option(
        False,
        "--json",
        help="Output results as JSON.",
    ),
    output: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Save results to JSON file.",
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

    scanner = TCPScanner(
        timeout=timeout,
        workers=workers,
    )

    start = time.perf_counter()

    results = []

    with Progress(
        SpinnerColumn(),
        TextColumn(
            "[progress.description]{task.description}"
        ),
        BarColumn(),
        console=console,
    ) as progress:

        task = progress.add_task(
            "Scanning ports...",
            total=len(selected_ports),
        )

        for port in selected_ports:
            result = scanner.scan_port(
                resolved_target,
                port,
            )

            results.append(result)

            progress.update(
                task,
                advance=1,
            )

    duration = time.perf_counter() - start

    results.sort(
        key=lambda item: item.port,
    )

    if output:
        write_json(
            results,
            output,
        )

        console.print(
            f"[green]Saved JSON output:[/green] {output}"
        )

    if json_output:
        console.print(
            to_json(results)
        )
        raise typer.Exit()

    console.print(
        Panel(
            f"""
[cyan]Target:[/cyan] {target}
[cyan]Resolved:[/cyan] {resolved_target}
[cyan]Ports:[/cyan] {len(selected_ports)}
[cyan]Workers:[/cyan] {workers}
[cyan]Timeout:[/cyan] {timeout}s
            """.strip(),
            title="PortScout Scan",
            border_style="cyan",
        )
    )

    table = Table(
        title="Scan Results",
    )

    table.add_column("PORT")
    table.add_column("STATUS")
    table.add_column("SERVICE")
    table.add_column("RESPONSE")

    for result in results:
        table.add_row(
            str(result.port),
            (
                "[green]OPEN[/green]"
                if result.is_open
                else "[red]CLOSED[/red]"
            ),
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
        Panel(
            f"""
[green]Completed[/green]

Ports scanned: {len(results)}
Open ports: {len(open_ports)}
Duration: {duration:.2f}s
            """.strip(),
            title="Summary",
            border_style="green",
        )
    )