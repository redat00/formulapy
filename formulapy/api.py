"""formulapy Ergast API interaction module."""

from typing import List

from dacite import from_dict
from requests import get
from formulapy.helpers import find_key_in_dict

from formulapy.models import DriverStanding, ConstructorStanding, Result, Round


class ErgastAPI:
    """ErgastAPI Class"""

    ERGAST_URL = "http://ergast.com/api/f1"
    ERGAST_URL_PARAMS = "?limit=150"

    def __init__(self) -> None:
        """ErgastAPI init."""
        pass

    def get_rounds(self, year: int) -> List[Round]:
        """Get list of rounds for a specific year.

        Args:
            year: Int representation of a year

        Returns:
            List[Round]: A list of Round object
        """
        data = get(f"{self.ERGAST_URL}/{year}.json{self.ERGAST_URL_PARAMS}")
        return [
            from_dict(data_class=Round, data=round)
            for round in list(find_key_in_dict(data.json(), "Races"))[0]
        ]

    def get_results(self, year: int, round: int) -> List[Result]:
        """Get results for a specific year and round.

        Args:
            year: int representation of a year
            round: int representation of a round number

        Returns:
            List[Result]: A list of generated Result object
        """
        data = get(
            f"{self.ERGAST_URL}/{year}/{round}"
            f"/results.json{self.ERGAST_URL_PARAMS}"
        )
        return [
            from_dict(data_class=Result, data=result)
            for result in list(find_key_in_dict(data.json(), "Results"))[0]
        ]

    def get_driver_standings(self, year: int) -> List[DriverStanding]:
        """Get a driver standings.

        Args:
            year: Int representation of a year

        Returns:
            List[DriverStanding]: A full drivers standing
        """
        data = get(
            f"{self.ERGAST_URL}/{year}/"
            f"driverStandings.json{self.ERGAST_URL_PARAMS}"
        )
        return [
            from_dict(data_class=DriverStanding, data=standing)
            for standing in list(
                find_key_in_dict(data.json(), "DriverStandings")
            )[0]
        ]

    def get_constructor_standings(
        self, year: int
    ) -> List[ConstructorStanding]:
        """Get a constructor standings.

        Args:
            year: Int representation of a year

        Returns:
            List[ConstructorStanding]: A full constructor standings
        """
        data = get(
            f"{self.ERGAST_URL}/{year}"
            f"/constructorStandings.json{self.ERGAST_URL_PARAMS}"
        )
        return [
            from_dict(data_class=ConstructorStanding, data=standing)
            for standing in list(
                find_key_in_dict(data.json(), "ConstructorStandings")
            )[0]
        ]


if __name__ == "__main__":
    ergast = ErgastAPI()
    for stand in ergast.get_constructor_standings(2022):
        print(stand)
