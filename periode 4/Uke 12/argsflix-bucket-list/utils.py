from operator import attrgetter
from typing import Iterable, TypeVar

T = TypeVar("T")


def multisort(iterable: Iterable[T], sort_specs: list[tuple[str, bool]]) -> list[T]:
    for sort_by, reverse in reversed(sort_specs):
        iterable = sorted(iterable, key=attrgetter(sort_by), reverse=reverse)
    return iterable


# multisort(list(student_objects), (("grade", True), ("age", False)))
