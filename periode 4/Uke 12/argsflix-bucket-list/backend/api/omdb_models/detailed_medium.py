from pydantic import Field, field_validator

from .base_medium import BaseMedium
from .rating import Rating


class DetailedMedium(BaseMedium):
    pg_rating: str = Field(alias="Rated")
    released: str = Field(alias="Released")
    runtime: str = Field(alias="Runtime")
    genre: list[str] = Field(alias="Genre")
    director: list[str] = Field(alias="Director")
    writer: list[str] = Field(alias="Writer")
    actors: list[str] = Field(alias="Actors")
    plot: str = Field(alias="Plot")
    language: list[str] = Field(alias="Language")
    country: list[str] = Field(alias="Country")
    awards: str = Field(alias="Awards")
    ratings: list[Rating] = Field(alias="Ratings")
    metascore: str = Field(alias="Metascore")
    imdb_rating: str = Field(alias="imdbRating")
    imdb_votes: int = Field(alias="imdbVotes")

    @field_validator(
        "genre", "director", "writer", "actors", "language", "country", mode="before"
    )
    @classmethod
    def listify(cls, raw: str) -> list[str]:
        return raw.split(", ")

    @field_validator("ratings", mode="before")
    @classmethod
    def parse_ratings(cls, raw: list[dict]) -> list[Rating]:
        return [Rating(**rating) for rating in raw]

    @field_validator("imdb_votes", mode="before")
    @classmethod
    def parse_comma_integer(cls, raw: str) -> int:
        return int(raw.replace(",", ""))
