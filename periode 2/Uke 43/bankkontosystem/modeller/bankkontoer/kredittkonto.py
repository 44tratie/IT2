from modeller.person import Person

from .bankkonto import Bankkonto


class Kredittkonto(Bankkonto):
    _MIN_SALDO = -5000

    def __init__(self, eier: Person, kontonummer: str, start_saldo: float = 0) -> None:
        super().__init__(eier, kontonummer, start_saldo)

    def _har_nok_saldo(self, beløp: float) -> bool:
        if self.saldo - beløp < Kredittkonto._MIN_SALDO:
            print(f"Du kan ikke ta uttaket på {beløp:.2f} kr!")
            return False

        return True
