import csv
import os

from klasser import Bestilling, Eple, KjøperBestilling, Mel, Produkt


def få_produktoppføringer() -> list[Produkt]:
    oppføringer = []

    with open(
        absolutt_bane("offentlig/produktoppføring.csv"), encoding="utf-8-sig"
    ) as oppføringsfil:
        data = csv.DictReader(oppføringsfil, delimiter=";")

        for produkt in data:
            match produkt["Type"]:
                case "Mel":
                    oppføringer.append(Mel(**produkt))
                case "Eple":
                    oppføringer.append(Eple(**produkt))
                case _:
                    raise Exception("du troller")

    return oppføringer


def få_bestillinger() -> list[Bestilling]:
    with open(
        absolutt_bane("offentlig/bestillinger.csv"), encoding="utf-8-sig"
    ) as bestillingsfil:
        data = csv.reader(bestillingsfil, delimiter=";")

        person_bestillinger: list[Bestilling] = []
        for linje in data:
            if linje[1].count("Mobil"):
                navn = linje[0]
                mobil = linje[1].split(": ")[1]
                person_bestillinger.append(Bestilling(navn, mobil, []))
                continue

            if not linje[0] or not linje[1]:
                continue

            produkt = linje[0]
            mengde = int("".join(linje[1].split()[:-1]))

            person_bestillinger[-1].bestillinger.append(
                KjøperBestilling(produkt, mengde)
            )

    return person_bestillinger


def absolutt_bane(relativ_bane: str) -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), relativ_bane)


def main() -> None:
    få_bestillinger()


if __name__ == "__main__":
    main()
