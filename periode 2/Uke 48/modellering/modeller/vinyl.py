from .album import Album


class Vinyl(Album):
    def __init__(
        self,
        navn: str,
        artist: str,
        plateselskap: str,
        utgivelsesår: int,
        rpm: int,
        farge: str,
    ) -> None:
        super().__init__(navn, artist, plateselskap, utgivelsesår)
        self.rpm = rpm
        self.farge = farge

    def __str__(self) -> str:
        return f"{self.navn} ({self.utgivelsesår}) via {self.plateselskap} (Vinyl, rpm: {self.rpm}, farge: {self.farge})"
