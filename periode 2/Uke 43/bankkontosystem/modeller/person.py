from dataclasses import dataclass
from functools import cached_property

from landskode import Landskode


@dataclass
class Person:
    fornavn: str
    etternavn: str
    telefonnummer: str
    landskode: Landskode = Landskode.NO

    @cached_property
    def navn(self) -> str:
        return f"{self.fornavn} {self.etternavn}"

    @cached_property
    def internasjonal_nummer(self) -> str:
        return f"{self.landskode} {self.telefonnummer}"
