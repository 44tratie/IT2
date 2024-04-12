from pydantic import Field

from .detailed_medium import DetailedMedium


class DetailedSeries(DetailedMedium):
    """Models the response of id search from the OMDb API where type is series"""

    total_seasons: int = Field(alias="totalSeasons")
