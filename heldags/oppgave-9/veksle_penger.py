from collections import defaultdict
from functools import wraps
from typing import Callable

Veksel = dict[int, int] # {mynt_verdi: antall, ...}

def påkrev_sedler(f):
    """Påkrever at beløpet består av 200-, 100- og 50-lapper.

    Returns
    -------
    Callable[[int], Veksel]
        En dekorert funksjon som kun godtar beløper med seddelkriteriumet.
    """
    
    @wraps(f)
    def wrapper(beløp: int):
        opprinnelig_beløp = beløp

        while beløp >= 200:
            beløp -= 200

        while beløp >= 100:
            beløp -= 100

        while beløp >= 50:
            beløp -= 50
        
        if beløp != 0:
            print("Beløpet kan ikke deles fullstendig med 200-, 100- og 50-lapper.")
            return {}

        return f(opprinnelig_beløp)

    return wrapper

@påkrev_sedler
def veksle_penger(beløp: int) -> Veksel:
    """Veksler et beløp til mynter.
    Det returnerede objektet inneholder antall mynter til visse myntverdier.
    Antall mynter skal minimeres med hjelp av 20, 10, 5 og 1 kroninger.

    Parameters
    ----------
    beløp : int
        Beløpet som skal veksles til mynter

    Returns
    -------
    Veksel
        En ordbok som inneholder hvor mange mynter det er av visse verdier.
    """

    veksel = defaultdict(int)

    if beløp > 500:
        return veksel
    
    while beløp >= 20:
        beløp -= 20
        veksel[20] += 1

    while beløp >= 10:
        beløp -= 10
        veksel[10] += 1

    while beløp >= 5:
        beløp -= 5
        veksel[5] += 1

    while beløp >= 1:
        beløp -= 1
        veksel[1] += 1

    return veksel
