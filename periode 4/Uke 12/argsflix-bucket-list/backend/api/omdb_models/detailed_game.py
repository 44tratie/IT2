from pydantic import Field

from .detailed_medium import DetailedMedium


class DetailedGame(DetailedMedium):
    """Models the response of id search from the OMDb API where type is game"""

    dvd: str = Field(alias="DVD")
    box_office: str = Field(alias="BoxOffice")
    production: str = Field(alias="Production")
    website: str = Field(alias="Website")
