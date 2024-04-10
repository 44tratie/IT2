from pydantic import Field, field_validator

from .detailed_medium import DetailedMedium


class DetailedMovie(DetailedMedium):
    dvd: str = Field(alias="DVD")
    box_office: str = Field(alias="BoxOffice")
    production: str = Field(alias="Production")
