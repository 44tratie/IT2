from pydantic import BaseModel, Field


class Bil(BaseModel):
    """Modellerer en bil"""

    type: str = Field(alias="Type")
    modell: str = Field(alias="Modell")
    registreringsnummer: str = Field(alias="Registreringsnummer")
    pris_per_km: float = Field(alias="Pris per km")

    def lever(self, km_kjørt: float):
        print(f"Pris for strekningen {km_kjørt} km: {self.pris_per_km * km_kjørt}")

    def __str__(self) -> str:
        data = self.model_dump(by_alias=True)
        # streng = f"Type: {self.__class__.__name__}\n"
        streng = ""
        for nøkkel, verdi in data.items():
            streng += f"{nøkkel}: {verdi}\n"

        return streng
