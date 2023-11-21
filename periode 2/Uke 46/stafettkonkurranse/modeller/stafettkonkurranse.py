from .lag import Lag
from .person import Person


class Stafettkonkurranse:
    """Modellerer en stafettkonkurranse

    Parameters
    ----------
    lag : list[Lag]
        Navnet til personen
    eksplisitt_løpetid : float, optional
        Tiden det tar for en person å løpe, dersom det er fastsatt

    Methods
    -------
    løp()
        Returnerer tiden det tok for et løp
    """

    def __init__(self, lag: list[Lag], dommere: list[Person]) -> None:
        """Oppretter en instans av en stafettkonkurranse

        Parameters
        ----------
        lag : list[Lag]
            Lagene i konkurransen
        dommere : list[Person]
            Dommerene/tidførerne/arrangørene av konkurransen
        """

        self.lag = lag
        self.dommere = dommere

    @staticmethod
    def print_vinner(resultater: list[float]) -> None:
        """Gitt en liste med tider, printer laget som løp raskest og tiden deres

        Parameters
        ----------
        resultater : list[float]
            Listen med tider
        """

        raskest_tid = min(resultater)
        raskest_lag = resultater.index(raskest_tid)

        print(f"Lag {raskest_lag + 1} vant! ({raskest_tid / 1000} s)")

    def gjør_løp(self) -> list[float]:
        """Simulerer et stafettløp for alle deltagende lag

        Returns
        -------
        list[float]
            En liste med tider over hvor raskt hvert enkelt lag løp til sammen
        """

        tid_tabell = []

        for i, lag in enumerate(self.lag, start=1):
            lag_tid = 0
            print(f"Lag {i} løper")

            for spiller in lag.spillere:
                tid = spiller.løp()
                print(f"{spiller} løp på {tid / 1000} sekunder!")
                lag_tid += tid

            print(f"Lag {i} løp på {lag_tid / 1000} sekunder")
            print()

            tid_tabell.append(lag_tid)

        return tid_tabell

    def __str__(self) -> str:
        output = "Stafettkonkurranse\n"
        output += "Dommere:\n"
        output += ", ".join(map(str, self.dommere))
        output += "\n"

        for i, lag in enumerate(self.lag, start=1):
            output += f"Lag {i}:\n"
            output += ", ".join(map(str, lag.spillere))
            output += "\n"

        return output
