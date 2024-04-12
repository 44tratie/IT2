from pydantic import BaseModel, Field


class Rating(BaseModel):
    """Models a rating that is used within responses from the OMDb API"""

    source: str = Field(alias="Source")
    value: str = Field(alias="Value")
