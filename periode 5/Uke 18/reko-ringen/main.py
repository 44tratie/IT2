from collections import defaultdict

from klasser import Bestilling, Produkt
from verktøy import få_bestillinger, få_produktoppføringer


def vis_oppføringer(oppføringer: list[Produkt]) -> None:
    print("Oppføringer:")
    for oppføring in oppføringer:
        print(oppføring)


def vis_bestillinger(bestillinger: list[Bestilling]) -> None:
    print("Bestillinger:")
    for bestilling in bestillinger:
        print(bestilling)


def vis_total(oppføringer: list[Produkt], bestillinger: list[Bestilling]) -> None:
    total_oversikt = defaultdict(int)

    for bestilling in bestillinger:
        for kunde_bestilling in bestilling.bestillinger:
            total_oversikt[kunde_bestilling.produkt] += kunde_bestilling.mengde

    total_fortjeneste = 0

    for produkt, total_mengde in total_oversikt.items():
        for oppføring in oppføringer:
            if oppføring.navn == produkt:
                break

        fortjeneste = total_mengde * oppføring.kilopris
        total_fortjeneste += fortjeneste

        print(f"{produkt}: {total_mengde} kg ({fortjeneste} kr)")

    print(f"Total fortjeneste: {total_fortjeneste} kr")


def main() -> None:
    oppføringer = få_produktoppføringer()
    bestillinger = få_bestillinger()

    print(oppføringer)
    print(bestillinger)

    vis_oppføringer(oppføringer)
    vis_bestillinger(bestillinger)
    vis_total(oppføringer, bestillinger)


if __name__ == "__main__":
    main()
