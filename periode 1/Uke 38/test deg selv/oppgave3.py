Butikknavn = str
Varepriser = dict[Butikknavn, int]


# snake_case er konvensjon ovenfor camelCase i python.
def finn_butikk(
    handleliste: set[str], prislister: list[Varepriser], butikker: list[Butikknavn]
) -> Butikknavn:
    pris_sum = [
        sum([pris for vare, pris in prisliste.items() if vare in handleliste])
        for prisliste in prislister
    ]
    return butikker[pris_sum.index(min(pris_sum))]


def finn_butikk_2(handleliste: set[str], prislister: dict[Butikknavn, Varepriser]):
    pris_sum = {
        butikk: sum([pris for vare, pris in prisliste.items() if vare in handleliste])
        for butikk, prisliste in prislister.items()
    }
    return min(pris_sum, key=pris_sum.get)


def main() -> None:
    handleliste = ["salat", "melk"]
    prisliste = [
        {"salat": 12, "fisk": 99, "melk": 12, "brod": 12},
        {"salat": 22, "fisk": 60, "melk": 18, "brod": 21},
        {"salat": 8, "fisk": 120, "melk": 10, "brod": 19},
        {"salat": 18, "fisk": 40, "melk": 30, "brod": 59},
        {"salat": 15, "fisk": 200, "melk": 40, "brod": 9},
    ]
    butikker = ["Rema1000", "Meny", "Kiwi", "Spar", "Joker"]

    # ----
    print(finn_butikk(handleliste, prisliste, butikker))

    # ---- deloppgave b
    prisliste = {
        "Rema1000": {"salat": 12, "fisk": 99, "melk": 12, "brod": 12},
        "Meny": {"salat": 22, "fisk": 60, "melk": 18, "brod": 21},
        "Kiwi": {"salat": 8, "fisk": 120, "melk": 10, "brod": 19},
        "Spar": {"salat": 18, "fisk": 40, "melk": 30, "brod": 59},
        "Joker": {"salat": 15, "fisk": 200, "melk": 40, "brod": 9},
    }
    print(finn_butikk_2(handleliste, prisliste))


def unit_tests() -> None:
    print("----------------------")
    print("unit tests starter her")
    prislister = {
        "1": {"a": 0, "b": 2, "c": 4, "d": 6},
        "2": {"a": 1, "b": 1, "c": 1, "d": 100}
    }
    assert finn_butikk_2(["a"], prislister) == "1"
    assert finn_butikk_2(["b"], prislister) == "2"
    assert finn_butikk_2(["c"], prislister) == "2"
    assert finn_butikk_2(["d"], prislister) == "1"
    assert finn_butikk_2(["b", "c"], prislister) == "2"
    assert finn_butikk_2(["a", "b", "c", "d"], prislister) == "1"

    print("alle unit testsa passerte!")

if __name__ == "__main__":
    main()
    unit_tests()
