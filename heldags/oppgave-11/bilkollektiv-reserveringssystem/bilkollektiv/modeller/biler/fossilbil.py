from .bil import Bil

from pydantic import Field

class Fossilbil(Bil):
    """Modellerer en fossilbil"""

    bensin_per_km: float = Field(alias="Bensin per km")
    tank: int = Field(alias="Tank")
    drivstoffmengde: int = Field(alias="Drivstoffmengde")