import functools
import json
import os
import shutil
import time
from typing import Self

from .api.omdb_models import BaseMedium


class BucketList:
    """The bucket list in this application.
    This class will grab the newest local data at any initialization point in code."""

    def __init__(self) -> None:
        self.list: dict[str, BaseMedium]
        self.seen: set[str]
        # grabs newest local data
        self._load_list()
        self._load_seen()

    @staticmethod
    def _save_list(method):
        """Saves the list locally after calling the method"""

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
        """Loads the bucket list from local data"""

        with open("bucket_list.json") as local_bucket_list:
            try:
                # load the local data
                local_media = json.load(local_bucket_list)
                # deserialize data back to pydantic models
                self.list = {
                    key: BaseMedium(**json.loads(local_media[key]))
                    for key in local_media
                }
            except json.JSONDecodeError:
                # local json file is corrupt! resetting
                self.reset_list(is_corrupt=True)

    def _save_seen(self) -> None:
        """Saves seen ids locally"""

        with open("seen.json", "w") as local_seen_list:
            json.dump(list(self.seen), local_seen_list)

    def _load_seen(self) -> None:
        """Loads local seen ids"""

        with open("seen.json") as local_seen_list:
            try:
                local_seen = json.load(local_seen_list)
                # deserialize back to set
                self.seen = set(local_seen)
            except json.JSONDecodeError:
                # json file is corrupt! resetting
                self.reset_list(is_corrupt=True)

    @_save_list
    def add_to_list(self, new_entry: BaseMedium):
        """Adds a new entry containing the base details of a medium to the bucket list"""

        self.list[new_entry.imdb_id] = new_entry

    @_save_list
    def remove_from_list(self, entry_id: str):
        """Removes an entry (using id) from the bucket list"""

        self.list.pop(entry_id, None)

    @_save_list
    def reset_list(self, is_corrupt: bool = False):
        """Resets the bucket list"""

        # stores corrupt files in case of user error
        if is_corrupt:
            os.makedirs("corrupt")
            shutil.copy("bucket_list.json", f"corrupt/bucket_list{time.time()}.json")
            shutil.copy("seen.json", f"corrupt/seen{time.time()}.json")

        # resets the list
        self.list = {}
        self.seen = set()
        self._save_seen()

    def update_seen(self, entry_id: str):
        """Flips the seen-state of a medium id"""

        if entry_id in self.seen:
            self.seen.remove(entry_id)
        else:
            self.seen.add(entry_id)

        self._save_seen()
