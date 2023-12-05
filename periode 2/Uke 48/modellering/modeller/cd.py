from .album import Album


class CD(Album):
    def __init__(
        self, navn: str, artist: str, plateselskap: str, utgivelsesår: int
    ) -> None:
        super().__init__(navn, artist, plateselskap, utgivelsesår)

    def __str__(self) -> str:
        return f"{self.navn} ({self.utgivelsesår}) via {self.plateselskap} (CD)"
