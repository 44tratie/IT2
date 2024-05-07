import json
from typing import Any

from .modeller.biler import Elbil, Fossilbil, Bil
from settings import bildata_bane

class BilKollektiv:
    def __init__(self) -> None:
        # dict[registreringsnummer, Bil]
        self.biler: dict[str, Bil] = {}

        with open(bildata_bane, encoding="utf-8") as bildata_fil:
            data: list[dict[str, Any]] = json.load(bildata_fil)

            print(data)

            # Deserialisering, innlasting av objekter
            for bil in data:
                match bil["Type"]:
                    case "Elbil":
                        self.biler[bil["Registreringsnummer"]] = Elbil(**bil)
                    case "Fossil":
                        self.biler[bil["Registreringsnummer"]] = Fossilbil(**bil)
    
    def vis_biler(self):
        for bil in self.biler.values():
            print(bil)

    def lagre_tilstand(self):
        # Serialisering
        json_data = [bil.model_dump(by_alias=True) for bil in self.biler.values()]

        with open(bildata_bane, "w") as bildata_fil:
            json.dump(json_data, bildata_fil)


    