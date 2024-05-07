from collections import defaultdict

from bilkollektiv import BilKollektiv
from bilkollektiv.modeller.biler import Elbil, Fossilbil
from .reservasjon import Reservasjon

class Reserveringssystem:
    def __init__(self, bilkollektiv: BilKollektiv, simulasjon: bool = False) -> None:
        self.simulasjon = simulasjon
        self.bilkollektiv = bilkollektiv

        # dict[id, Reservasjon]
        self.reservasjoner: dict[int, Reservasjon] = {}
        # dict[bil_registreringsnummer, reservasjoner]
        self.bil_reservasjoner: dict[str, dict[int, Reservasjon]] = defaultdict(dict)

    def legg_til_reservasjon(self, reservasjon: Reservasjon):
        # Bilen finnes ikke i kollektivet
        if reservasjon.bil_registreringsnummer not in self.bilkollektiv.biler:
            return
        
        # Bilen er allerede reservert på det tidspunktet
        for bil_reservasjon in self.bil_reservasjoner.get(reservasjon.bil_registreringsnummer, {}).get(reservasjon.reservasjon_ID, []):
            if reservasjon.overlapper(bil_reservasjon):
                return
            # uimplementert
            # if dato_overlapp(reservasjon, bil_reservasjon):
                # return
            pass

        self.reservasjoner[reservasjon.reservasjon_ID] = reservasjon
        self.bil_reservasjoner[reservasjon.bil_registreringsnummer][reservasjon.reservasjon_ID] = reservasjon

    def fjern_reservasjon(self, reservasjon_ID: int):
        self.bil_reservasjoner[self.reservasjoner[reservasjon_ID].bil_registreringsnummer].pop(reservasjon_ID)
        self.reservasjoner.pop(reservasjon_ID)

    def lever_bil(self, reservasjon: Reservasjon, km_kjørt: float):
        bil_kjørt = self.bilkollektiv.biler[reservasjon.bil_registreringsnummer]

        print(f"Pris for strekningen {km_kjørt}: {bil_kjørt.pris_per_km * km_kjørt}")

        match bil_kjørt:
            # Antar at brukeren fullader/fyller tanken helt opp hvis den noen gang ble brukt opp
            case Elbil():
                wattimer_forbruk = bil_kjørt.wattimer_per_km * km_kjørt
                print(f"Du har brukt {wattimer_forbruk} watt-timer av bilen")

                if bil_kjørt.energinivå < wattimer_forbruk:
                    print("Du fulladet bilen ved kjøring")
                    bil_kjørt.energinivå += bil_kjørt.batteri

                bil_kjørt.energinivå -= wattimer_forbruk

                print(f"Bilen har {bil_kjørt.energinivå} watt-timer igjen")
            case Fossilbil():
                bensin_forbruk = bil_kjørt.bensin_per_km * km_kjørt
                print(f"Du har brukt {bensin_forbruk} liter av bilens tank")

                if bil_kjørt.drivstoffmengde < bensin_forbruk:
                    print("Du fylte bilens tank ved kjøring")
                    bil_kjørt.drivstoffmengde += bil_kjørt.tank

                bil_kjørt.drivstoffmengde -= bensin_forbruk

                print(f"Bilen har {bil_kjørt.drivstoffmengde} liter bensin igjen")

        # Oppdater tilstanden til bilene
        if not self.simulasjon:
            self.bilkollektiv.lagre_tilstand()