"""formulapy helpers module."""


from typing import List, Union
from rich.table import Table
from click import Abort, echo


tables_list = {
    "driver_standings": [
        "Position",
        "Driver",
        "Constructor",
        "Wins",
        "Points",
    ],
    "constructor_standings": ["Position", "Constructor", "Wins", "Points"],
    "race_results": [
        "Position",
        "Driver",
        "Constructor",
        "Finished",
        "Points",
    ],
    "races_listing": ["Number", "Race", "Circuit", "Time"],
}


def _feed_drivers_standings_table(
    type: str, table: Table, data: list
) -> Table:
    """Feed data inside table.

    Args:
        table: A Table object ready to be filled
        data: List of data to feed inside table

    Returns:
        Table: A fed table
    """
    table.title = "Driver Standings"
    for column in tables_list[type]:
        table.add_column(column)
    for driver in data:
        table.add_row(
            driver.position,
            driver.Driver.get_formatted_name(),
            driver.Constructors[0].name,
            driver.wins,
            driver.points,
        )
    return table


def _feed_constructors_standings_table(
    type: str, table: Table, data: list
) -> Table:
    """Feed data inside table.

    Args:
        table: A Table object ready to be filled
        data: List of data to feed inside table

    Returns:
        Table: A fed table
    """
    table.title = "Constructor Standings"
    for column in tables_list[type]:
        table.add_column(column)
    for constructor in data:
        table.add_row(
            constructor.position,
            constructor.Constructor.name,
            constructor.wins,
            constructor.points,
        )
    return table


def _feed_race_results_table(type: str, table: Table, data: list) -> Table:
    """Feed data inside table.

    Args:
        table: A Table object ready to be filled
        data: List of data to feed inside table

    Returns:
        Table: A fed table
    """
    table.title = "Race Result"
    for column in tables_list[type]:
        table.add_column(column)
    for result in data:
        table.add_row(
            result.position,
            result.Driver.get_formatted_name(),
            result.Constructor.name,
            result.status,
            result.points,
        )
    return table


def _feed_races_listing_table(type, table: Table, data: list) -> Table:
    """Feed data inside table.

    Args:
        table: A Table object ready to be filled
        data: List of data to feed inside table

    Returns:
        Table: A fed table
    """
    table.title = "Races"
    for column in tables_list[type]:
        table.add_column(column)
    for race in data:
        table.add_row(
            race.round, race.raceName, race.Circuit.circuitName, race.date
        )
    return table


def generate_table(type: str, data: list) -> Table:
    """Generate table based on type and data.

    Args:
        type: str representation of a type in tables_list
        data: List of data to be append to table

    Returns:
        Table: Fully loaded ready to be output Table object
    """
    table = Table(title="test")
    match type:
        case "driver_standings":
            table = _feed_drivers_standings_table(type, table, data)
        case "constructor_standings":
            table = _feed_constructors_standings_table(type, table, data)
        case "race_results":
            table = _feed_race_results_table(type, table, data)
        case "races_listing":
            table = _feed_races_listing_table(type, table, data)
        case _:
            echo(f"{type} is not valid!", err=True)
            raise Abort()
    return table


def find_key_in_dict(data: dict, search_pattern: str) -> Union[List, dict]:
    """Will find a key in a dict and return it's value.

    Args:
        data: Dict you want to search in
        search_pattern: Pattern to look for inside of dict

    Returns:
        Union[List, dict]: The found element that can be a list or a dict
    """
    if hasattr(data, "items"):
        for k, v in data.items():
            if k == search_pattern:
                yield v
            if isinstance(v, dict):
                for result in find_key_in_dict(v, search_pattern):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in find_key_in_dict(d, search_pattern):
                        yield result
