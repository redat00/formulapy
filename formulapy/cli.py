"""formulapy CLI module."""


from click import group, pass_context, argument, pass_obj
from formulapy.api import ErgastAPI
from formulapy.helpers import generate_table
from rich.console import Console


@group
@pass_context
def cli(ctx):
    """Init of cli.

    Args:
        ctx: Context of click
    """
    ctx.obj = ErgastAPI()


@cli.command
@argument("year", required=True)
@pass_obj
def rounds(obj: ErgastAPI, year: int) -> None:
    """Get rounds for a specific year.

    Args:
        obj: Instantiated ErgastAPI object
        year: Int reprensatation of a year
    """
    console = Console()
    console.print(
        generate_table(type="races_listing", data=obj.get_rounds(year))
    )


@cli.command
@argument("year", required=True)
@pass_obj
def driver_standing(obj: ErgastAPI, year: int) -> None:
    """Get driver standing for a specific year.

    Args:
        obj: Instantiated ErgastAPI object
        year: Int reprensation of a year
    """
    console = Console()
    console.print(
        generate_table(
            type="driver_standings", data=obj.get_driver_standings(year)
        )
    )


@cli.command
@argument("year", required=True)
@pass_obj
def constructor_standing(obj: ErgastAPI, year: int) -> None:
    """Get constructor standing for a specific year.

    Args:
        obj: Instantiated ErgastAPI object
        year: Int reprensation of a year
    """
    console = Console()
    console.print(
        generate_table(
            type="constructor_standings",
            data=obj.get_constructor_standings(year),
        )
    )


@cli.command
@argument("year", required=True)
@argument("round", required=True)
@pass_obj
def race_result(obj: ErgastAPI, year: int, round: int):
    """Get race result for a specific year and round.

    Args:
        ctx: Context of click
        year: Int representation of a year
        round: Int representation of a round
    """
    console = Console()
    console.print(
        generate_table(
            type="race_results",
            data=obj.get_results(year, round),
        )
    )
