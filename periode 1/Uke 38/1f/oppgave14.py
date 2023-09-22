def word_counter(text: str) -> int:
    """Counts the amount of words in a text

    Parameters
    ----------
    text : str
        The text

    Returns
    -------
    int
        The amount of words the text contains
    """

    return len(text.split())


def main() -> None:
    text = "this is a text."
    assert word_counter(text) == 4


if __name__ == "__main__":
    main()
