"""formulapy models module."""

from dataclasses import dataclass
from typing import Optional, List

# All along those files you will see that variables names are not PEP8
# compliant, this is because I use dacite package, which allow me to load a
# dataclass object from a dictionnary, but only if name correspond to what the
# dict is set with.
# Since the ErgastAPI uses a camelCase notation, my dataclasses needs it too.


@dataclass
class Time:
    """Time object model."""

    millis: Optional[str]
    time: str


@dataclass
class AverageSpeed:
    """AverageSpeed object model."""

    units: str
    speed: str


@dataclass
class Location:
    """Location object model."""

    lat: str
    long: str
    locality: str
    country: str


@dataclass
class Circuit:
    """Circuit object model."""

    circuitId: str
    url: str
    circuitName: str
    Location: Location


@dataclass
class Round:
    """Round object model."""

    season: str
    round: str
    raceName: str
    Circuit: Circuit
    date: str


@dataclass
class Driver:
    """Driver object model."""

    driverId: str
    permanentNumber: str
    code: str
    url: str
    givenName: str
    familyName: str
    dateOfBirth: str
    nationality: str

    def get_formatted_name(self) -> str:
        """Get formatted name.

        Returns:
            str: Formatted name (eg. "Fernando Alonso")
        """
        return f"{self.givenName} {self.familyName}"


@dataclass
class Constructor:
    """Constructor object model."""

    constructorId: str
    url: str
    name: str
    nationality: str


@dataclass
class FastestLap:
    """FastestLap object model."""

    rank: str
    lap: str
    Time: Time
    AverageSpeed: AverageSpeed


@dataclass
class Result:
    """Result object model."""

    number: str
    position: str
    points: str
    Driver: Driver
    Constructor: Constructor
    grid: str
    laps: str
    status: str
    Time: Optional[Time]
    FastestLap: Optional[FastestLap]


@dataclass
class DriverStanding:
    """DriverStanding object model.

    This is not a full driver leaderboard, it is only an entry!
    A List[DriverStanding] will be a full standing.
    """

    position: str
    points: str
    wins: str
    Driver: Driver
    Constructors: List[Constructor]


@dataclass
class ConstructorStanding:
    """ConstructorStanding object model.

    This is not a full driver leaderboard, it is only an entry!
    A List[ConstructorStanding] will be a full standing.
    """

    position: str
    points: str
    wins: str
    Constructor: Constructor
