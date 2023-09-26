def minst(liste: list[int | float]) -> int | float:
    """Henter det minste tallet fra en liste

    Parameters
    ----------
    liste : list[int  |  float]
        Listen med tall

    Returns
    -------
    int | float
        Det minste tallet
    """

    return min(liste)

try:
    assert minst([1, 2, 3]) == 1
    assert minst([2]) == 2
    assert minst([1.5, 2.5]) == 1.5
except AssertionError:
    print("OBS: funksjonen \"minst\" kan gi feil svar!")