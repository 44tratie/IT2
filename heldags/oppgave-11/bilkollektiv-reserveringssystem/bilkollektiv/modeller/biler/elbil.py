from .bil import Bil

from pydantic import Field

class Elbil(Bil):
    """Modellerer en elbil"""

    wattimer_per_km: int = Field(alias="Watt-timer per km")
    batteri: int = Field(alias="Batteri")
    energinivå: int = Field(alias="Energinivå")