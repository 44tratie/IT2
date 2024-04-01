from operator import attrgetter
from typing import Iterable


def multisort(iterable: Iterable, sort_specs: list[tuple[str, bool]]):
    for sort_by, reverse in reversed(sort_specs):
        iterable = sorted(iterable, key=attrgetter(sort_by), reverse=reverse)
    return iterable


# multisort(list(student_objects), (("grade", True), ("age", False)))
