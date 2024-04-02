from typing import Literal

from pydantic import BaseModel, Field, field_validator

from .missing_poster import BLANK_FILE_SVG


class BaseMedium(BaseModel):
    title: str = Field(alias="Title")
    year: str = Field(alias="Year")
    imdb_id: str = Field(alias="imdbID")
    type_: Literal["movie", "series", "game"] = Field(alias="Type")
    poster: str = Field(alias="Poster")

    @field_validator("poster", mode="before")
    @classmethod
    def validate_url(cls, raw: str) -> str:
        return raw if raw != "N/A" else BLANK_FILE_SVG
