from .person import Person


class Lag:
    """Modellerer et lag

    Parameters
    ----------
    spillere : list[Person]
        Spillerene på laget
    """

    def __init__(self, spillere: list[Person]) -> None:
        """Oppretter en instans av et lag

        Parameters
        ----------
        spillere : list[Person]
            Spillerene på laget
        """

        self.spillere = spillere
