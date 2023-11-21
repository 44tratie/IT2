from .person import Person


class Jente(Person):
    """Modellerer ei jente

    Parameters
    ----------
    navn : str
        Navnet til jenta
    eksplisitt_løpetid : float, optional
        Tiden det tar for en person å løpe, dersom det er fastsatt

    Methods
    -------
    løp()
        Returnerer tiden det tok for et løp
    """

    _min_tid = 11500
    _maks_tid = 13500

    def __init__(self, navn: str, eksplisitt_løpetid: float = None) -> None:
        super().__init__(navn, eksplisitt_løpetid)
