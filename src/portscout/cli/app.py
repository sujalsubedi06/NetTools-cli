"""
Main CLI application.
"""

from __future__ import annotations

import typer

from portscout import __version__

app = typer.Typer(
    name="portscout",
    help="A modern Python network reconnaissance toolkit.",
    no_args_is_help=True,
    add_completion=False,
)


@app.callback()
def main() -> None:
    """PortScout CLI."""
    return


@app.command()
def version() -> None:
    """Display the current PortScout version."""
    typer.echo(f"PortScout v{__version__}")