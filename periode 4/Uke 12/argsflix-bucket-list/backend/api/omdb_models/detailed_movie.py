from pydantic import Field, field_validator

from .detailed_medium import DetailedMedium


class DetailedMovie(DetailedMedium):
    """Models the response of id search from the OMDb API where type is movie"""

    dvd: str = Field(alias="DVD")
    box_office: str = Field(alias="BoxOffice")
    production: str = Field(alias="Production")
