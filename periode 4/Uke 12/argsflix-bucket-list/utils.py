import functools
import os
import shutil
from operator import attrgetter
from typing import Iterable, TypeVar

T = TypeVar("T")


def multisort(iterable: Iterable[T], sort_specs: list[tuple[str, bool]]) -> list[T]:
    for sort_by, reverse in reversed(sort_specs):
        iterable = sorted(iterable, key=attrgetter(sort_by), reverse=reverse)
    return iterable


def test_environment(test_f):
    @functools.wraps(test_f)
    def wrapped(*args, **kwargs):
        # store existing values in temp files
        os.makedirs("temp")
        shutil.copy("bucket_list.json", "temp/bucket_list.json")
        shutil.copy("seen.json", "temp/seen.json")

        # code is not expected to crash but in case of CTRL C
        try:
            return_val = test_f(*args, **kwargs)
        finally:
            # restore existing values
            shutil.copy("temp/seen.json", "seen.json")
            shutil.copy("temp/bucket_list.json", "bucket_list.json")
            shutil.rmtree("temp")

            return return_val

    return wrapped
