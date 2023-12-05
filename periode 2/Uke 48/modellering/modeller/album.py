class Album:
    def __init__(
        self, navn: str, artist: str, plateselskap: str, utgivelsesår: int
    ) -> None:
        self.navn = navn
        self.artist = artist
        self.plateselskap = plateselskap
        self.utgivelsesår = utgivelsesår

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(f'{key}={value}' for key, value in self.__dict__.items())})"
