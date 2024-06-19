ReeltTall = float | int


# Metodene i klassen er statiske da de ikke avhenger av en instanse
class Kalkulator:
    """En kalkulator med enkle statiske metoder for aritmetiske operasjoner (+, -, *, /)"""

    # For å håndtere desimaltallfeil i ganging og deling
    MAKS_DESIMALER: int = 5

    @staticmethod
    def pluss(a: ReeltTall, b: ReeltTall) -> ReeltTall:
        return a + b

    @staticmethod
    def minus(a: ReeltTall, b: ReeltTall) -> ReeltTall:
        return a - b

    @staticmethod
    def gange(a: ReeltTall, b: ReeltTall) -> ReeltTall:
        return round(a * b, Kalkulator.MAKS_DESIMALER)

    @staticmethod
    def dele(a: ReeltTall, b: ReeltTall) -> ReeltTall:
        # Velger å returnere None for ugyldige parametre
        # alternativer kunne vært å raise ValueError.
        if b == 0:
            return
        return round(a / b, Kalkulator.MAKS_DESIMALER)
