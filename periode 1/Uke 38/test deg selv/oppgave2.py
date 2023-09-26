from string import ascii_letters

ascii_letters += "æøåÆØÅ"
LETTERS = set(ascii_letters)

def gyldig_alder(alder: str, print_errors: bool=True) -> bool:
    try:
        alder = int(alder)
        assert alder > 0
        return True
    except (ValueError, TypeError):
        if print_errors:
            print("ugyldig tall")
        return False
    except AssertionError:
        if print_errors:
            print("alder må være positivt")
        return False

def gyldig_bokstav(bokstav: str, print_errors: bool=True) -> bool:
    try:
        assert bokstav in LETTERS
        return True
    except AssertionError:
        if print_errors:
            print("du skrev ikke en bokstav")
        return False


def be_om_alder() -> int:
    alder = input("Alder: ")
    while not gyldig_alder(alder):
        alder = input("Alder: ")
    return alder


def be_om_bokstav() -> str:
    bokstav = input("Skriv en bokstav: ")
    while bokstav is None:
        bokstav = input("Skriv en bokstav: ")
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


def unit_tests() -> None:
    print("-----------------------")
    print("her starter unit tests!")

    # gyldig alder test
    assert not gyldig_alder("1.5", print_errors=False)
    assert not gyldig_alder("1,5", print_errors=False)
    assert not gyldig_alder("abc", print_errors=False)
    assert not gyldig_alder("-1", print_errors=False)
    assert not gyldig_alder("-1.5", print_errors=False)
    assert gyldig_alder("2", print_errors=False)

    # gyldig bokstavtest
    assert not gyldig_bokstav("abc", print_errors=False)
    assert not gyldig_bokstav("ABC", print_errors=False)
    assert not gyldig_bokstav("-", print_errors=False)
    assert gyldig_bokstav("æ", print_errors=False)
    assert gyldig_bokstav("A", print_errors=False)

    print("programmet passerte alle test cases!")

if __name__ == "__main__":
    main()
    unit_tests()
