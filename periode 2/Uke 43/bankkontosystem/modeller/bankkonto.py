class Bankkonto:
    def __init__(self, eiernavn: str, kontonummer: str, start_saldo: float = 0) -> None:
        self.eiernavn = eiernavn
        self.kontonummer = kontonummer
        self.saldo = start_saldo

    def innskudd(self, beløp: float) -> bool:
        if beløp <= 0:
            print("Du kan bare ha innskudd på mer enn 0 kr!")
            return False

        self.saldo += beløp
        print(f"Du satte inn {beløp:.2f} kr")
        self._vis_ny_saldo()
        return True

    def uttak(self, beløp: float) -> bool:
        if not self._har_nok_saldo(beløp):
            self._vis_saldo()
            return False

        self.saldo -= beløp
        print(f"Du tok ut {beløp:.2f} kr")
        self._vis_ny_saldo()
        return True

    def _har_nok_saldo(self, beløp: float) -> bool:
        if self.saldo < beløp:
            print(f"Du kan ikke ta uttaket på {beløp:.2f} kr!")
            return False

        return True

    def _vis_ny_saldo(self) -> None:
        print(f"Ny saldo er {self.saldo:.2f} kr\n")

    def _vis_saldo(self) -> None:
        print(f"Du har {self.saldo:.2f} kr på kontoen\n")

    def __str__(self) -> str:
        return f"""Konto:
\t{"Eier":<15}: {self.eiernavn}
\t{"Kontonummer":<15}: {self.kontonummer}
\t{"Saldo":<15}: {self.saldo:.2f}\n"""
