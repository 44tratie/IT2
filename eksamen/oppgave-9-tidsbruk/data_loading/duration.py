from dataclasses import dataclass
from typing import Self


@dataclass
class Duration:
    """A representation of a time duration from the dataset"""

    hours: int
    minutes: int

    @classmethod
    def from_string(cls, raw: str) -> Self:
        """Constructs a Duration-object from a string (where the format is "hours.minutes")

        Parameters
        ----------
        raw : str
            The raw string, e.g. "2.50" for 2 hours and 50 minutes

        Returns
        -------
        Self
            An instance of Duration with the given data
        """

        hours, minutes = map(int, raw.split("."))
        return cls(hours, minutes)

    def total_seconds(self) -> int:
        """Get the total amount of seconds

        Returns
        -------
        int
            The total amount of seconds
        """

        return self.hours * 3600 + self.minutes * 60

    def total_minutes(self) -> int:
        """Get the total amount of minutes

        Returns
        -------
        int
            The total amount of minutes
        """

        return self.hours * 60 + self.minutes

    def __str__(self) -> str:
        """String representation of the duration in "#h #m" format

        Returns
        -------
        str
            The string representation of the duration
        """
        return f"{self.hours}h {self.minutes}m"
