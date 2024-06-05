from pydantic import Field

from .bil import Bil


class Fossilbil(Bil):
    """Modellerer en fossilbil"""

    bensin_per_km: float = Field(alias="Bensin per km")
    tank: int = Field(alias="Tank")
    drivstoffmengde: int = Field(alias="Drivstoffmengde")

    def lever(self, km_kjørt: float):
        bensin_forbruk = self.bensin_per_km * km_kjørt
        print(f"Du har brukt {bensin_forbruk} liter av bilens tank")

        if self.drivstoffmengde < bensin_forbruk:
            print("Du fylte bilens tank ved kjøring")
            self.drivstoffmengde += self.tank

        self.drivstoffmengde -= bensin_forbruk

        print(f"Bilen har {self.drivstoffmengde} liter bensin igjen")

        return super().lever(km_kjørt)
