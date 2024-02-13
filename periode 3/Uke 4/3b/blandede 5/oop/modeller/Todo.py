from pydantic import BaseModel, Field


class Todo(BaseModel):
    bruker_id: int = Field(alias="userId")
    id: int
    tittel: str = Field(alias="title")
    er_fullført: bool = Field(alias="completed")

    def __str__(self) -> str:
        return f"Oppgave {self.id} (Bruker {self.bruker_id})\t- {self.tittel}"
