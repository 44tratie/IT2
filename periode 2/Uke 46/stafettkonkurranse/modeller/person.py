import random


class Person:
    """Modellerer en person

    Parameters
    ----------
    navn : str
        Navnet til personen
    eksplisitt_løpetid : float, optional
        Tiden det tar for en person å løpe, dersom det er fastsatt

    Methods
    -------
    løp()
        Returnerer tiden det tok for et løp
    """

    _min_tid = 1e4
    _maks_tid = 2e4

    def __init__(self, navn: str, eksplisitt_løpetid: float = None) -> None:
        """Oppretter en instanse av person

        Parameters
        ----------
        navn : str
            Navnet til personen
        eksplisitt_løpetid : float, optional
            Tiden det tar for en person å løpe, dersom det er fastsatt
        """

        self.navn = navn
        self.eksplisitt_løpetid = eksplisitt_løpetid

    def løp(self) -> float:
        """Simulerer et 100 meter løp

        Returns
        -------
        float
            Hvor raskt i millisekunder det tok for personen å fullføre et 100 meter løp
        """

        if self.eksplisitt_løpetid is not None:
            return self.eksplisitt_løpetid

        return random.randint(self._min_tid, self._maks_tid)

    def __str__(self) -> str:
        return self.navn
