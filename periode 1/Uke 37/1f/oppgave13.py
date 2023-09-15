def letter_count(letter: str, text: str, case_sensitive: bool = True) -> int:
    """Counts the amount of times a letter appears in a text

    Parameters
    ----------
    letter : str
        The letter to search for
    text : str
        The text to search in
    case_sensitive : bool, optional
        Whether the search is case sensitive, by default True

    Returns
    -------
    int
        The frequency count of the letter
    """
    if not case_sensitive:
        letter = letter.lower()
        text = text.lower()
    return text.count(letter)


def main() -> None:
    print(letter_count("a", "denne setningen har fire forekomster av bokstaven a"))
    print(letter_count("A", "denne setningen har kun en forekomst av bokstaven A"))


if __name__ == "__main__":
    main()
