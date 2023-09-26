def størst(liste: list[int | float]) -> int | float:
    """Henter det største tallet fra en liste

    Parameters
    ----------
    liste : list[int  |  float]
        Listen med tall

    Returns
    -------
    int | float
        Det største tallet
    """

    return max(liste)

try:
    assert størst([1, 2, 3]) == 3
    assert størst([2]) == 2
    assert størst([1.5, 2.5]) == 2.5
except AssertionError:
    print("OBS: funksjonen \"størst\" kan gi feil svar!")