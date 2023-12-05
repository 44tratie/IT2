from .platesamling import Platesamling


class Eier:
    def __init__(self, navn: str) -> None:
        self.navn = navn
        self.platesamling = Platesamling()
