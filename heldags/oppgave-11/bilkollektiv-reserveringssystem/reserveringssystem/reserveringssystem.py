import json
from collections import defaultdict
from datetime import UTC, datetime

from bilkollektiv import BilKollektiv
from settings import reservasjonsdata_bane

from .reservasjon import Reservasjon


class Reserveringssystem:
    def __init__(self, bilkollektiv: BilKollektiv, simulasjon: bool = False) -> None:
        self.simulasjon = simulasjon
        self.bilkollektiv = bilkollektiv

        with open(reservasjonsdata_bane) as reservasjonsdata_fil:
            reservasjonsdata_json = json.load(reservasjonsdata_fil)

        # dict[id, Reservasjon]
        self.reservasjoner: dict[int, Reservasjon] = reservasjonsdata_json[
            "reservasjoner"
        ]
        # dict[bil_registreringsnummer, reservasjoner]
        self.bil_reservasjoner: dict[str, dict[int, Reservasjon]] = defaultdict(dict)
        self.bil_reservasjoner.update(reservasjonsdata_json["bil_reservasjoner"])

        self.neste_reservasjon_id = (
            (
                max(
                    self.reservasjoner,
                    key=lambda k: self.reservasjoner[k].reservasjon_ID,
                )
                + 1
            )
            if self.reservasjoner
            else 1
        )

    def vis_ledige_biler(self, start_tid: datetime, slutt_tid: datetime) -> set[str]:
        ledige_biler = {
            reg_nr
            for reg_nr in self.bilkollektiv.biler.keys()
            if all(
                not bil_reservasjon.overlapper(start_tid, slutt_tid)
                for bil_reservasjon in self.bil_reservasjoner[reg_nr].values()
            )
        }

        print(f"Ledige biler: {", ".join(ledige_biler)}")

        return ledige_biler

    def få_reservasjoner(self) -> list[Reservasjon]:
        return [
            reservasjon
            for reservasjon in self.reservasjoner.values()
            if reservasjon.start_tid > datetime.now(UTC)
        ]

    def få_utløpte_reservasjoner(self) -> list[Reservasjon]:
        return [
            reservasjon
            for reservasjon in self.reservasjoner.values()
            if reservasjon.start_tid < datetime.now(UTC)
        ]

    def lag_reservasjon(
        self,
        navn: str,
        email: str,
        bil_registreringsnummer: str,
        start_tid: datetime,
        slutt_tid: datetime,
    ):
        reservasjon = Reservasjon(
            self.neste_reservasjon_id,
            navn,
            email,
            bil_registreringsnummer,
            start_tid,
            slutt_tid,
        )

        # Bilen finnes ikke i kollektivet
        if reservasjon.bil_registreringsnummer not in self.bilkollektiv.biler:
            return

        # Bilen er allerede reservert på det tidspunktet
        for bil_reservasjon in self.bil_reservasjoner.get(
            reservasjon.bil_registreringsnummer, {}
        ).values():
            if reservasjon.overlapper(
                bil_reservasjon.start_tid, bil_reservasjon.slutt_tid
            ):
                return

        self.reservasjoner[reservasjon.reservasjon_ID] = reservasjon
        self.bil_reservasjoner[reservasjon.bil_registreringsnummer][
            reservasjon.reservasjon_ID
        ] = reservasjon

        self.neste_reservasjon_id += 1

        print("Kvittering:")
        print(reservasjon)

        self.lagre_reservasjoner()

    def fjern_reservasjon(self, reservasjon_ID: int):
        self.bil_reservasjoner[
            self.reservasjoner[reservasjon_ID].bil_registreringsnummer
        ].pop(reservasjon_ID)
        self.reservasjoner.pop(reservasjon_ID)

        self.lagre_reservasjoner()

    def lever_bil(self, reservasjon: Reservasjon, km_kjørt: float):
        bil_kjørt = self.bilkollektiv.biler[reservasjon.bil_registreringsnummer]

        bil_kjørt.lever(km_kjørt)

        # Oppdater tilstanden til bilene
        if not self.simulasjon:
            self.bilkollektiv.lagre_tilstand()

    def lagre_reservasjoner(self):
        if self.simulasjon:
            return

        # Serialisering
        reservasjoner = {
            reservasjon_id: reservasjon.model_dump_json()
            for reservasjon_id, reservasjon in self.reservasjoner.items()
        }
        bil_reservasjoner = {
            reg_nr: {
                reservasjon_id: reservasjon.model_dump_json()
                for reservasjon_id, reservasjon in reservasjoner.items()
            }
            for reg_nr, reservasjoner in self.bil_reservasjoner.items()
        }

        with open(reservasjonsdata_bane, "w") as reservasjonsdata_fil:
            json.dump(
                {
                    "reservasjoner": reservasjoner,
                    "bil_reservasjoner": bil_reservasjoner,
                },
                reservasjonsdata_fil,
            )
