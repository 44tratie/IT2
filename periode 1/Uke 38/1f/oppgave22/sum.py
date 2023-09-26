def summer(liste: list[int | float]) -> float:
    """Summerer tallene i en liste

    Parameters
    ----------
    liste : list[int  |  float]
        Listen med tall

    Returns
    -------
    float
        Summen av tallene i listen
    """    

    return sum(liste)

try:
    assert summer([1, 2, 3]) == (1 + 2 + 3)
    assert summer([2]) == (2)
    assert summer([1.5, 2.5]) == (1.5 + 2.5)
except AssertionError:
    print("OBS: funksjonen \"summer\" kan gi feil svar!")