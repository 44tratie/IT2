from dataclasses import dataclass


@dataclass
class KjøperBestilling:
    produkt: str
    mengde: int


@dataclass
class Bestilling:
    kjøper: str
    mobil: str
    bestillinger: list[KjøperBestilling]

    def __str__(self) -> str:
        streng = f"Kjøper: {self.kjøper} ({self.mobil})\n"

        for bestilling in self.bestillinger:
            streng += f"{bestilling.produkt}\t({bestilling.mengde} kg)\n"

        return streng
