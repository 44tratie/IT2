from typing import Literal

from .album import Album
from .cd import CD
from .vinyl import Vinyl


class Artist:
    def __init__(self, navn) -> None:
        self.navn = navn
        self.album: list[Album] = []

    def registrer_vinyl(
        self,
        album_navn: str,
        plateselskap: str,
        utgivelsesår: int,
        rpm: int,
        farge: str,
    ) -> None:
        self.album.append(
            Vinyl(album_navn, self.navn, plateselskap, utgivelsesår, rpm, farge)
        )

    def registrer_cd(
        self,
        album_navn: str,
        plateselskap: str,
        utgivelsesår: int,
    ) -> None:
        self.album.append(CD(album_navn, self.navn, plateselskap, utgivelsesår))

    def hent_album(
        self,
        album_navn: str,
    ) -> Album | None:
        for album in self.album:
            if album.navn == album_navn:
                return album
        print(f"fant ikke albumet '{album_navn}' under artisten {self.navn}!")
        print(f"Registrerte ")
        return None

    def __str__(self) -> str:
        output = ""

        output += f"Registrerte album for artisten {self.navn}:\n\n"
        output += "\n".join(map(str, self.album))

        return output
