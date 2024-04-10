from pydantic import Field

from .detailed_medium import DetailedMedium


class DetailedSeries(DetailedMedium):
    total_seasons: int = Field(alias="totalSeasons")
