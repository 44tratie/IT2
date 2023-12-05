from .album import Album
from .artist import Artist


class Platesamling:
    def __init__(self) -> None:
        self.album: set[Album] = set()

    @property
    def artister(self) -> set[str]:
        artister = set()
        for album in self.album:
            artister.add(album.artist)
        return artister

    def legg_til_artist(self, artist: Artist) -> None:
        self.album.update(artist.album)

    def legg_til_album(self, album: Album) -> None:
        self.album.add(album)

    def __str__(self) -> str:
        output = "Platesamling:\n\n"

        for album in self.album:
            output += f"{str(album)}\n"

        return output.strip()  # fjerne excess newline
