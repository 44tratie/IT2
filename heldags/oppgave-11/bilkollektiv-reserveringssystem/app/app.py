from datetime import UTC, datetime
from typing import Callable

from reserveringssystem import Reservasjon, Reserveringssystem


class App:
    def __init__(self, reserveringssystem: Reserveringssystem) -> None:
        self.reserveringssystem = reserveringssystem
        self.kjører = False

    def kjør(self) -> None:
        self.kjører = True

        while self.kjører:
            self._vis_meny(
                [
                    ("Avslutt", self._avslutt),
                    ("Reserver", self._reserver),
                    ("Avbestill", self._avbestill),
                    ("Lever bil", self._lever_bil),
                ]
            )

    def _avslutt(self):
        self.kjører = False

    def _reserver(self):
        start_t = datetime.fromisoformat(input("Start tid (ISO 8601): ")).astimezone(
            UTC
        )
        while start_t < datetime.now(UTC):
            print("Du kan ikke reservere før dags dato")
            start_t = datetime.fromisoformat(
                input("Start tid (ISO 8601): ")
            ).astimezone(UTC)

        slutt_t = datetime.fromisoformat(input("Slutt tid (ISO 8601): ")).astimezone(
            UTC
        )
        while slutt_t < start_t:
            print("Slutt tid må være etter start tid")
            slutt_t = datetime.fromisoformat(
                input("Slutt tid (ISO 8601): ")
            ).astimezone(UTC)

        ledige_biler = self.reserveringssystem.vis_ledige_biler(start_t, slutt_t)
        if not ledige_biler:
            print("Ingen biler finnes for dette tidsrommet")
            return

        bil = input("Bilnummer: ")
        while bil not in ledige_biler:
            print("Bilen er ikke ledig eller finnes ikke")
            bil = input("Bilnummer: ")

        navn = input("Navnet ditt: ")
        email = input("Emailen din: ")

        self.reserveringssystem.lag_reservasjon(navn, email, bil, start_t, slutt_t)

    def _avbestill(self):
        reservasjoner = self.reserveringssystem.få_reservasjoner()

        if not reservasjoner:
            print("Ingen reservasjoner funnet")
            return

        for i, reservasjon in enumerate(reservasjoner, start=1):
            print(
                f"{i}:\t{reservasjon.bil_registreringsnummer} ({reservasjon.start_tid} - {reservasjon.slutt_tid})"
            )

        valg_i = App._få_bruker_valg(len(reservasjoner)) - 1

        self.reserveringssystem.fjern_reservasjon(reservasjoner[valg_i].reservasjon_ID)

    def _lever_bil(self):
        reservasjoner = self.reserveringssystem.få_utløpte_reservasjoner()

        if not reservasjoner:
            print("Ingen reservasjoner funnet")
            return

        for i, reservasjon in enumerate(reservasjoner, start=1):
            print(
                f"{i}:\t{reservasjon.bil_registreringsnummer} ({reservasjon.start_tid} - {reservasjon.slutt_tid})"
            )

        valg_i = App._få_bruker_valg(len(reservasjoner)) - 1

        reservasjon = reservasjoner[valg_i]
        self.reserveringssystem.lever_bil(reservasjon)
        self.reserveringssystem.fjern_reservasjon(reservasjon.reservasjon_ID)

    @staticmethod
    def _vis_meny(handlinger: list[tuple[str, Callable]]):
        for i, handling in enumerate(handlinger, start=1):
            print(f"{i}:\t{handling[0]}")

        valg_i = App._få_bruker_valg(len(handlinger)) - 1

        handlinger[valg_i][1]()

    @staticmethod
    def _få_bruker_valg(
        maks_indeks: int, min_indeks: int = 1, melding: str = "Skriv inn: "
    ) -> int:
        while True:
            try:
                valg = int(input(melding))
                if min_indeks <= valg <= maks_indeks:
                    return valg
                raise ValueError
            except ValueError:
                print(f"Svaret må være et heltall mellom {min_indeks} og {maks_indeks}")
