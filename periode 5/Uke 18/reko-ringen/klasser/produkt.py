from pydantic import BaseModel, Field


class Produkt(BaseModel):
    """Modellerer et produkt"""

    navn: str = Field(alias="Navn")
    kilopris: int = Field(alias="Kilopris (kroner)")

    def __str__(self) -> str:
        data = self.model_dump(by_alias=True)
        streng = f"Type: {self.__class__.__name__}\n"

        for nøkkel, verdi in data.items():
            streng += f"{nøkkel}: {verdi}\n"

        return streng
