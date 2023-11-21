import random

from .gutt import Gutt
from .jente import Jente
from .lag import Lag
from .person import Person


class Idrettslag:
    """Modellerer et idrettslag

    Parameters
    ----------
    gutter : list[Gutt]
        En liste over guttene i idrettslaget
    jenter : list[Jente]
        En liste over jentene i idrettslaget

    Methods
    -------
    trekk_to_lag()
        Returnerer to lag med de spesifiserte antallene gutter og jenter
    """

    def __init__(self, gutter: list[Gutt], jenter: list[Jente]) -> None:
        """Oppretter en instans av et idrettslag

        Parameters
        ----------
        gutter : list[Gutt]
            Guttene i idrettslaget
        jenter : list[Jente]
            Jentene i idrettslaget
        """

        self.gutter = gutter
        self.jenter = jenter

    def trekk_to_lag(
        self, antall_gutter: int, antall_jenter: int
    ) -> tuple[tuple[Lag, Lag], list[Person]]:
        """Trekker to lag fra idrettslaget

        Parameters
        ----------
        antall_gutter : int
            Antallet gutter som skal være på hvert lag
        antall_jenter : int
            Antallet jenter som skal være på hvert lag

        Returns
        -------
        tuple[tuple[Lag, Lag], list[Person]]
            Returnerer de to lagene sammen i en tuple, og en liste av lagløse personer
        """

        if not self._kan_lage_to_lag(antall_gutter, antall_jenter):
            return Lag([]), Lag([])

        # Scrambler medlemslisten for å få tilfeldige lag
        gutter = random.sample(self.gutter, len(self.gutter))
        jenter = random.sample(self.jenter, len(self.jenter))

        # Lager lagene med indeksering
        lag_1 = Lag(gutter[:antall_gutter] + jenter[:antall_jenter])
        lag_2 = Lag(
            gutter[antall_gutter : antall_gutter * 2]
            + jenter[antall_jenter : antall_jenter * 2]
        )

        # Resten er lagløse spillere
        rest = gutter[antall_gutter * 2 :] + jenter[antall_jenter * 2 :]

        return (lag_1, lag_2), rest

    def _kan_lage_to_lag(self, antall_gutter: int, antall_jenter: int) -> bool:
        """Sjekker om man har nok gutter og jenter på idrettslaget til å lage 2 lag

        Parameters
        ----------
        antall_gutter : int
            Antall gutter som skal være på hvert lag
        antall_jenter : int
            Antall jenter som skal være på hvert lag

        Returns
        -------
        bool
            Om to lag kan lages eller ikke
        """

        if antall_gutter * 2 > len(self.gutter):
            print(f"Har ikke nok gutter for å lage 2 lag med {antall_gutter} gutter")
            return False
        if antall_jenter * 2 > len(self.jenter):
            print(f"Har ikke nok jenter for å lage 2 lag med {antall_jenter} jenter")
            return False

        return True
