from string import ascii_letters

LETTERS = set(ascii_letters)


def be_om_alder() -> int:
    alder = None
    while alder is None:
        try:
            alder = int(input("Alder: "))
        except ValueError:
            print("ugyldig tall")
    return alder


def be_om_bokstav() -> str:
    bokstav = None
    while bokstav is None:
        try:
            bokstav = input("Skriv en bokstav: ")
            assert bokstav in LETTERS
        except AssertionError:
            print("du skrev ikke en bokstav")
            bokstav = None
    return bokstav


def main() -> None:
    personer: dict[str, int] = {}

    fortsett = True
    while fortsett:
        navn = input("Navn: ")
        alder = be_om_alder()

        personer[navn] = alder

        fortsett_query = input("skriv 'j' for å fortsette: ").lower()
        fortsett = fortsett_query == "j"

    første_bokstav = be_om_bokstav().lower()

    for navn, alder in personer.items():
        if navn[0].lower() == første_bokstav:
            print(f"{navn}, ({alder} år gammel)")


if __name__ == "__main__":
    main()
