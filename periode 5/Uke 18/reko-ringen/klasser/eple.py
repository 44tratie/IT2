from pydantic import Field

from .produkt import Produkt


class Eple(Produkt):
    """Modellerer et produkt"""

    farge: str = Field(alias="Farge")
