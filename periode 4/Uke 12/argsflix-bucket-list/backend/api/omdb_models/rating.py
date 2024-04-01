from pydantic import BaseModel, Field


class Rating(BaseModel):
    source: str = Field(alias="Source")
    value: str = Field(alias="Value")
