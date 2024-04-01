import os
from typing import Literal
from urllib.parse import urlencode

import requests

from .omdb_models import BaseMedium


class APIWrapper:
    BASE_URL = "https://www.omdbapi.com/?"

    def __init__(self) -> None:
        self.__api_key = os.environ.get("OMDB_API_KEY")

    def query_movie(
        self,
        search: str,
        type_: Literal["movie"] | Literal["series"] | None = None,
        year: int | None = None,
    ) -> list[BaseMedium]:
        query_params = {"s": search, "type": type_, "y": year, "apikey": self.__api_key}
        res = requests.get(
            self.BASE_URL
            + urlencode({k: v for k, v in query_params.items() if v is not None})
        )

        data = res.json()

        if data["Response"] != "True":
            return []

        return [BaseMedium(**entry) for entry in data["Search"]]
