from pydantic import Field

from .produkt import Produkt


class Mel(Produkt):
    """Modellerer et produkt"""

    best_før: str = Field(alias="Best før")
