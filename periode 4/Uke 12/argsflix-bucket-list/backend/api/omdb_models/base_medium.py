from typing import Literal

from pydantic import BaseModel, Field


class BaseMedium(BaseModel):
    title: str = Field(alias="Title")
    year: str = Field(alias="Year")
    imdb_id: str = Field(alias="imdbID")
    type_: Literal["movie", "series", "game"] = Field(alias="Type")
    poster: str = Field(alias="Poster")
