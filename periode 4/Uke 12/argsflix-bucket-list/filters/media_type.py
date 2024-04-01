from typing import Callable

from backend.api.omdb_models import BaseMedium

from .utils.make_filter import make_filter
from .utils.selectbox_enum import SelectboxEnum


class MediaType(SelectboxEnum):
    ALL = "All"
    MOVIE = "Movie"
    SERIES = "Series"
    GAME = "Game"


def gen_filter_type(type_filter: MediaType) -> Callable[[BaseMedium], bool]:
    def filter_type(medium: BaseMedium) -> bool:
        match type_filter:
            case MediaType.ALL:
                return True
            case MediaType.MOVIE:
                return medium.type_ == "movie"
            case MediaType.SERIES:
                return medium.type_ == "series"
            case MediaType.GAME:
                return medium.type_ == "game"

    return filter_type


def make_type_filter() -> tuple[str, Callable[[BaseMedium], bool]]:
    return make_filter("Type:", MediaType.options(), gen_filter_type)
