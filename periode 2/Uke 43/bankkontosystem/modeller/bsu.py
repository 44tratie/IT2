from verktøy import bruker_godkjennelse

from .bankkonto import Bankkonto


class BSU(Bankkonto):
    def __init__(
        self, eiernavn: str, kontonummer: str, maks_saldo: float, start_saldo: float = 0
    ) -> None:
        super().__init__(eiernavn, kontonummer, start_saldo)
        self.maks_saldo = maks_saldo

    def innskudd(self, beløp: float) -> bool:
        if beløp + self.saldo > self.maks_saldo:
            print(f"Du kan ikke ha mer enn {self.maks_saldo} kr på kontoen")
            self._vis_saldo()

            if self.saldo == self.maks_saldo:
                return False

            print("Vil du legge inn mellomlegget til maksgrensen? (ja/nei)")
            innskudd = self.maks_saldo - self.saldo
            print(f"Innskudd: {innskudd:.2f} kr")
            print(f"Du får tilbake: {beløp - innskudd:.2f} kr")

            if bruker_godkjennelse():
                print(f"Du får {beløp - innskudd:.2f} kr tilbake!")
                return super().innskudd(innskudd)

            return False

        return super().innskudd(beløp)
