import os

def hent_absolutt_bane(relativ_bane: str) -> str:
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), relativ_bane
)