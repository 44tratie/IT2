def sort_digits(num: int, reverse: bool = False) -> int:
    """Sorts a number by its digits

    Parameters
    ----------
    num : int
        The number to sort
    reverse : bool, optional
        If this parameter is true, a descending order will be returned. By default False

    Returns
    -------
    int
        The number sorted by its digits
    """

    # Converts the number to a string so that its sortable, sorts it and converts it back into an integer
    return int("".join(sorted(str(num), reverse=reverse)))


def kaprekars(num: int, _prev: int = None) -> int:
    """Performs Kaprekar's algorithm until a recurring value is found

    Parameters
    ----------
    num : int
        The initial number. Needs to be a 4 digit integer with at least two different digits
    _prev : int, optional
        The previous number in the recursion tree, this does not need to be passed in initially. By default None

    Returns
    -------
    int
        The recurring number that arises after a certain amount of iterations
    """

    # Checks if a recurring value has been found
    if num == _prev:
        return num

    # Sorts the numbers by their digits
    asc, desc = sort_digits(num), sort_digits(num, reverse=True)

    # Finds the new value to apply the same algorithmn on
    new = desc - asc

    return kaprekars(new, num)


def main() -> None:
    tall = 1234
    print(kaprekars(tall))


if __name__ == "__main__":
    main()
