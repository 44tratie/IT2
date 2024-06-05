from __future__ import annotations

from datetime import UTC, datetime
from typing import Any


class Reservasjon:
    def __init__(
        self,
        reservasjon_ID: int,
        navn: str,
        email: str,
        bil_registreringsnummer: str,
        start_tid: datetime,
        slutt_tid: datetime,
    ) -> None:
        self.reservasjon_ID = reservasjon_ID
        self.navn = navn
        self.email = email
        self.bil_registreringsnummer = bil_registreringsnummer
        self.start_tid = (
            datetime.fromisoformat(start_tid).astimezone(UTC)
            if isinstance(start_tid, str)
            else start_tid.astimezone(UTC)
        )
        self.slutt_tid = (
            datetime.fromisoformat(slutt_tid).astimezone(UTC)
            if isinstance(slutt_tid, str)
            else slutt_tid.astimezone(UTC)
        )

    def overlapper(self, start_tid: datetime, slutt_tid: datetime) -> bool:
        return (
            slutt_tid.astimezone(UTC) > self.start_tid
            and start_tid.astimezone(UTC) < self.slutt_tid
        )

    def model_dump_json(self) -> dict[str, Any]:
        return {
            "reservasjon_ID": self.reservasjon_ID,
            "navn": self.navn,
            "email": self.email,
            "bil_registreringsnummer": self.bil_registreringsnummer,
            "start_tid": self.start_tid.isoformat(),
            "slutt_tid": self.slutt_tid.isoformat(),
        }

    def __str__(self) -> str:
        return f"""Reservasjon {self.reservasjon_ID} ({self.start_tid.isoformat()} - {self.slutt_tid.isoformat()})
Reservert bil: {self.bil_registreringsnummer}
Navn: {self.navn}
Email: {self.email}"""
