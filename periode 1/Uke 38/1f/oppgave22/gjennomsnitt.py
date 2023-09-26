from sum import summer


def gjennomsnitt(liste: list[int | float]) -> float:
    """Tar gjennomsnittet av tallene i en liste

    Parameters
    ----------
    liste : list[int  |  float]
        Listen med tall

    Returns
    -------
    float
        Gjennomsnittet av tallene i listen
    """
    return summer(liste) / len(liste)

try:
    assert gjennomsnitt([1, 2, 3]) == (1 + 2 + 3) / 3
    assert gjennomsnitt([2]) == (2) / 1
    assert gjennomsnitt([1.5, 2.5]) == (1.5 + 2.5) / 2
except AssertionError:
    print("OBS: funksjonen \"gjennomsnitt\" kan gi feil svar!")