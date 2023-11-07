from typing import Self

from modeller.person import Person


class Bankkonto:
    def __init__(self, eier: Person, kontonummer: str, start_saldo: float = 0) -> None:
        self.eier = eier
        self.kontonummer = kontonummer
        self._saldo = start_saldo

    @property
    def saldo(self) -> float:
        return self._saldo

    @classmethod
    def fra_csv(cls, filbane: str, *args, **kwargs) -> Self:
        with open(filbane) as csv_fil:
            full_navn, landskode, tlfnummer, kontonummer = csv_fil.readline().split(",")

        navn = full_navn.split()
        fornavn = " ".join(navn[:-1])
        etternavn = navn[-1]
        eier = Person(fornavn, etternavn, tlfnummer, landskode)
        return cls(eier, kontonummer, *args, **kwargs)

    def innskudd(self, beløp: float) -> bool:
        if beløp <= 0:
            print("Du kan bare ha innskudd på mer enn 0 kr!")
            return False

        self._saldo += beløp
        print(f"Du satte inn {beløp:.2f} kr")
        self._vis_ny_saldo()
        return True

    def uttak(self, beløp: float) -> bool:
        if not self._har_nok_saldo(beløp):
            self._vis_saldo()
            return False

        self._saldo -= beløp
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
\t{"Eier":<15}: {self.eier.navn}
\t{"Telefonnummer":<15}: {self.eier.internasjonal_nummer}
\t{"Kontonummer":<15}: {self.kontonummer}
\t{"Saldo":<15}: {self.saldo:.2f}\n"""
