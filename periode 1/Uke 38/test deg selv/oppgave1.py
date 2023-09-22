# 1-2-3 Kaker

Tall = float | int
Mengde = tuple[Tall, str]  # (verdi, enhet)
Oppskrift = dict[str, int]  # {"ingrediens": Tall}


def oppskrift_fra_sukker(mengde: Tall) -> Oppskrift:
    return {"sukker": mengde, "mel": mengde * 2, "smør": mengde * 3}


def oppskrift_fra_mel(mengde: Tall) -> Oppskrift:
    return {"sukker": mengde / 2, "mel": mengde, "smør": mengde * 1.5}


def oppskrift_fra_smoer(mengde: Tall) -> Oppskrift:
    return {"sukker": mengde / 3, "mel": mengde / 3 * 2, "smør": mengde}


def skriv_oppskrift(sukker: Mengde, mel: Mengde, smør: Mengde) -> None:
    print(
        f"""Oppskrift på kaker
Du trenger:
{sukker[0]:.2f} {sukker[1]} sukker
{mel[0]:.2f} {mel[1]} mel
{smør[0]:.2f} {smør[1]} smør"""
    )


def bak_kaker(mengde: Tall) -> None:
    oppskriftsbaser = {
        "sukker": oppskrift_fra_sukker,
        "mel": oppskrift_fra_mel,
        "smør": oppskrift_fra_smoer,
    }

    basert_på = None
    while basert_på is None:
        try:
            basert_på = input(
                "Baser oppskriften på 'sukker', 'mel' eller 'smør': "
            ).lower()
            assert basert_på in {"sukker", "mel", "smør"}
        except AssertionError:
            print("skriv en gyldig basisingrediens!")
            basert_på = None

    ingredienser = oppskriftsbaser[basert_på](mengde)

    parametre = [
        (ingredienser["sukker"], "gram"),
        (ingredienser["mel"], "gram"),
        (ingredienser["smør"], "gram"),
    ]
    skriv_oppskrift(*parametre)


def main() -> None:
    bak_kaker(2)


if __name__ == "__main__":
    main()
