def konverter_til_binær(tall: int) -> str:
    """Konverterer et heltall om til en streng som representerer tallet i binær.

    Parameters
    ----------
    tall : int
        Tallet i titallsystemet som skal konverteres

    Returns
    -------
    str
        Tallet i totallsystemet uten prefiksen "0b"
    """
    # Kom på at denne metoden for konvertering til binær er "enklere" enn å gjøre det matematisk i etterkant
    binær_string = bin(tall)  # har en prefix "0b"
    uten_prefix = binær_string[2:]
    return uten_prefix


def skaff_heltall(min_verdi: int, maks_verdi: int) -> int:
    """Skaffer et heltall fra brukeren mellom grensene gitt

    Parameters
    ----------
    min_verdi : int
        Den minste verdien tallet kan være (inklusivt)
    maks_verdi : int
        Den største verdien tallet kan være (inklusivt)

    Returns
    -------
    int
        Et trygt tall som brukeren har gitt
    """
    while True:
        try:
            tall = int(input(f"Skriv et tall mellom {min_verdi} og {maks_verdi}: "))
            assert min_verdi <= tall <= maks_verdi
            return tall
        except AssertionError:
            print("Du skrev et tall utenfor området")
        except ValueError:
            print("Du skrev ikke et gyldig tall")


def main() -> None:
    tall = skaff_heltall(1, 64)
    konvertert = konverter_til_binær(tall)
    print(f"{tall} (base-10) er {konvertert} (base-2)")


if __name__ == "__main__":
    main()
