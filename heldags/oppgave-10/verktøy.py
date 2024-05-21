import os


def hent_absolutt_bane(relativ_bane: str) -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relativ_bane)


def hent_måned(date: str):
    """Hjelpefunksjon for å hente måned fra en streng.
    Problemet kunne også blitt løst med parsing til datetime objekter ved lesing av csv.
    """

    return date.split(".")[1]
