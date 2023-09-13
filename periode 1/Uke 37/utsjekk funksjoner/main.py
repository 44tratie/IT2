Numeric = int | float


class Point:
    """
    A model of a point in a 2d plane.

    Attributes
    ----------
    x : Numeric
        x-position of the point
    y : Numeric
        y-position of the point
    """

    def __init__(self, x: Numeric, y: Numeric) -> None:
        self.x = x
        self.y = y


def intervals_overlap(
    lower_1: Numeric,
    upper_1: Numeric,
    lower_2: Numeric,
    upper_2: Numeric,
    include_border: bool = False,
) -> bool:
    """
    Take two intervals [lower_1, upper_1] and [lower_2, upper_2]
    and check whether they overlap.

    Parameters
    ----------
    lower_1 : Numeric
        The lower bound of the first interval
    upper_1 : Numeric
        The upper bound of the first interval
    lower_2 : Numeric
        The lower bound of the second interval
    upper_2 : Numeric
        The upper bound of the second interval
    include_border : bool, optional
        Whether bordering ranges should count as overlap, by default False

    Returns
    -------
    bool
        Whether the intervals overlap
    """

    # Given two intervals:
    # a----b
    #   c----d
    # Checks whether one boundary is outside the opposite end of the other range

    if include_border:
        return not (upper_1 < lower_2 or upper_2 < lower_1)

    return not (upper_1 <= lower_2 or upper_2 <= lower_1)


def rectangles_overlap(
    bottom_left_1: Point,
    top_right_1: Point,
    bottom_left_2: Point,
    top_right_2: Point,
) -> bool:
    """
    Given two rectangles with their bottom-left and top-right corners,
    checks whether they overlap.

    Parameters
    ----------
    bottom_left_1 : Point
        A point of the bottom-left corner of rectangle 1
    top_right_1 : Point
        A point of the top-right corner of rectangle 1
    bottom_left_2 : Point
        A point of the bottom-left corner of rectangle 2
    top_right_2 : Point
        A point of the top-right corner of rectangle 2

    Returns
    -------
    bool
        Whether the rectangles overlap
    """

    # Check whether the x-ranges AND the y-ranges of the rectangles overlap

    return intervals_overlap(
        bottom_left_1.x,
        top_right_1.x,
        bottom_left_2.x,
        top_right_2.x,
    ) and intervals_overlap(
        bottom_left_1.y,
        top_right_1.y,
        bottom_left_2.y,
        top_right_2.y,
    )


def unit_test_intervals_overlap() -> None:
    # a---b
    #   c---d
    # => True
    assert intervals_overlap(1, 3, 2, 4)

    # a-------b
    #   c---d
    # => True
    assert intervals_overlap(1, 4, 2, 3)

    #   a---b
    # c---d
    # => True
    assert intervals_overlap(2, 4, 1, 3)

    # a---b
    #       c---d
    # => False
    assert not intervals_overlap(1, 2, 3, 4)


def unit_test_rectangles_overlap() -> None:
    #    |---|
    # |--|   |
    # |  |---|
    # |    |
    # |----|
    # => True
    assert rectangles_overlap(Point(1, 1), Point(3, 3), Point(2, 2), Point(4, 4))

    #    |--|
    # |--|  |--|
    # |  |  |  |
    # |--|  |--|
    #    |--|
    # => True
    assert rectangles_overlap(Point(1, 2), Point(4, 3), Point(2, 1), Point(3, 4))

    # |------------|
    # |            |
    # |   |---|    |
    # |   |   |    |
    # |   |---|    |
    # |            |
    # |------------|
    # => True
    assert rectangles_overlap(Point(1, 1), Point(4, 4), Point(2, 2), Point(3, 3))

    # |--|
    # |--|
    # |--|
    #
    # |----|
    # |    |
    # |----|
    # => False
    assert not rectangles_overlap(Point(1, 1), Point(4, 2), Point(2, 3), Point(3, 4))

    #      |--|
    # |----|  |
    # |    |  |
    # |    |  |
    # |----|  |
    #      |--|
    # => False
    assert not rectangles_overlap(Point(1, 2), Point(2, 3), Point(2, 1), Point(3, 4))


def main() -> None:
    unit_test_intervals_overlap()
    unit_test_rectangles_overlap()


if __name__ == "__main__":
    main()
