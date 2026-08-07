"""
Main CLI application.
"""

from __future__ import annotations

import typer

from portscout import __version__
from portscout.cli.dns import dns
from portscout.cli.scan import scan
from portscout.cli.web import inspect
from portscout.cli.subdomains import subdomains
from portscout.core.console import console


app = typer.Typer(
    name="portscout",
    help=(
        "A modern Python network reconnaissance toolkit.\n\n"
        "Designed for authorized network diagnostics and discovery."
    ),
    no_args_is_help=True,
    add_completion=False,
)


app.command(name="scan")(scan)

app.command(name="dns")(dns)

app.command(name="subdomains")(subdomains)

app.command(name="web")(inspect)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        "-V",
        help="Show PortScout version.",
    ),
) -> None:
    """
    PortScout command line interface.
    """

    if version:
        console.print(
            f"[bold cyan]PortScout[/bold cyan] "
            f"[green]v{__version__}[/green]"
        )
        raise typer.Exit()

    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())
        raise typer.Exit()


@app.command()
def version() -> None:
    """
    Display the current PortScout version.
    """

    console.print(
        f"[bold cyan]PortScout[/bold cyan] "
        f"[green]v{__version__}[/green]"
    )