from __future__ import annotations

from datetime import datetime


class Reservasjon:
    reservasjon_ID = 0

    def __init__(self, navn: str, email: str, bil_registreringsnummer: str, start_tid: datetime, slutt_tid: datetime) -> None:
        Reservasjon.reservasjon_ID += 1
        self.reservasjon_ID = Reservasjon.reservasjon_ID

        self.navn = navn
        self.email = email
        self.bil_registreringsnummer = bil_registreringsnummer
        self.start_tid = start_tid
        self.slutt_tid = slutt_tid

    def overlapper(self, annen: Reservasjon) -> bool:
        return annen.slutt_tid > self.start_tid and annen.start_tid < self.slutt_tid