from .bankkonto import Bankkonto


class Sparekonto(Bankkonto):
    def __init__(
        self,
        eiernavn: str,
        kontonummer: str,
        maks_antall_uttak: int,
        start_saldo: float = 0,
    ) -> None:
        super().__init__(eiernavn, kontonummer, start_saldo)
        self.maks_antall_uttak = maks_antall_uttak
        self._reset_antall_uttak()

    def uttak(self, beløp: float) -> bool:
        if self.gjenværende_uttak <= 0:
            print("Du kan ikke ta flere uttak i år!")
            self._vis_saldo()
            return False

        if super().uttak(beløp):
            self.gjenværende_uttak -= 1
            return True

        return False

    def _reset_antall_uttak(self) -> None:
        self.gjenværende_uttak = self.maks_antall_uttak
