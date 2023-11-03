from dataclasses import dataclass
from functools import cached_property

from landskode import Landskode


@dataclass
class Person:
    fornavn: str
    etternavn: str
    telefonnummer: str
    landskode: Landskode = Landskode.NO

    def __post_init__(self) -> None:
        self.fornavn = self.fornavn.strip().title()
        self.etternavn = self.etternavn.strip().title()
        self.telefonnummer = self.telefonnummer.strip()

    @cached_property
    def navn(self) -> str:
        return f"{self.fornavn} {self.etternavn}"

    @cached_property
    def internasjonal_nummer(self) -> str:
        return f"{self.landskode} {self.telefonnummer}"
