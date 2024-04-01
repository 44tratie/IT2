import functools
import json
from typing import Self

from .api.omdb_models import BaseMedium


class BucketList:
    def __init__(self) -> None:
        self.list: dict[str, BaseMedium]
        self.seen: set[str]
        self._load_list()
        self._load_seen()

    @staticmethod
    def _save_list(method):
        @functools.wraps(method)
        def wrapped(self: Self, *args, **kwargs):
            method(self, *args, **kwargs)
            with open("bucket_list.json", "w") as local_bucket_list:
                json.dump(
                    {
                        key: self.list[key].model_dump_json(by_alias=True)
                        for key in self.list
                    },
                    local_bucket_list,
                )

        return wrapped

    def _load_list(self) -> None:
        with open("bucket_list.json") as local_bucket_list:
            try:
                local_media = json.load(local_bucket_list)
                self.list = {
                    key: BaseMedium(**json.loads(local_media[key]))
                    for key in local_media
                }
            except json.JSONDecodeError:
                self.list = {}

    def _save_seen(self) -> None:
        with open("seen.json", "w") as local_seen_list:
            json.dump(list(self.seen), local_seen_list)

    def _load_seen(self) -> None:
        with open("seen.json") as local_seen_list:
            try:
                local_seen = json.load(local_seen_list)
                self.seen = set(local_seen)
            except json.JSONDecodeError:
                self.seen = set()

    @_save_list
    def add_to_list(self, new_entry: BaseMedium):
        self.list[new_entry.imdb_id] = new_entry

    @_save_list
    def remove_from_list(self, entry_id: str):
        self.list.pop(entry_id, None)

    def update_seen(self, entry_id: str):
        if entry_id in self.seen:
            self.seen.remove(entry_id)
        else:
            self.seen.add(entry_id)

        self._save_seen()
