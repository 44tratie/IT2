from typing import Callable

from backend.api.omdb_models import BaseMedium
from backend.bucket_list import BucketList

from .utils.make_filter import make_filter
from .utils.selectbox_enum import SelectboxEnum


class SeenStatus(SelectboxEnum):
    ALL = "All"
    SEEN = "Seen"
    UNSEEN = "Unseen"


def gen_filter_show(show_filter: SeenStatus) -> Callable[[BaseMedium], bool]:
    def filter_show(medium: BaseMedium) -> bool:
        bucket_list = BucketList()
        match show_filter:
            case SeenStatus.ALL:
                return True
            case SeenStatus.SEEN:
                return medium.imdb_id in bucket_list.seen
            case SeenStatus.UNSEEN:
                return medium.imdb_id not in bucket_list.seen

    return filter_show


def make_show_filter() -> tuple[str, Callable[[BaseMedium], bool]]:
    return make_filter("Show:", SeenStatus.options(), gen_filter_show)
