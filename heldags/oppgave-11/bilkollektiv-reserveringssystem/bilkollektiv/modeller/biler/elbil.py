from pydantic import Field

from .bil import Bil


class Elbil(Bil):
    """Modellerer en elbil"""

    wattimer_per_km: int = Field(alias="Watt-timer per km")
    batteri: int = Field(alias="Batteri")
    energinivå: int = Field(alias="Energinivå")

    def lever(self, km_kjørt: float):
        wattimer_forbruk = self.wattimer_per_km * km_kjørt
        print(f"Du har brukt {wattimer_forbruk} watt-timer av bilen")

        if self.energinivå < wattimer_forbruk:
            antall_fulladinger, rest = divmod(wattimer_forbruk, self.batteri)
            print(f"Du fulladet bilen {antall_fulladinger+1} gang(er) ved kjøring")
            self.energinivå = self.batteri - rest
        else:
            self.energinivå -= wattimer_forbruk

        print(f"Bilen har {self.energinivå} watt-timer igjen")

        return super().lever(km_kjørt)
