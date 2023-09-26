def tell_tegn(tekst: str) -> int:
    antall = 0
    for _ in tekst:
        antall += 1
    return antall


def midt_tegn(tekst: str) -> str:
    midt, rest = divmod(len(tekst), 2)
    # [n:n+1] for oddetall, [n-1:n+1] for partall hvor n = len(tekst) // 2
    tekst_slice = slice(midt if rest else midt - 1, midt + 1)
    return tekst[tekst_slice]


def er_palindrom(tekst: str) -> bool:
    tekst = tekst.lower()
    return tekst == tekst[::-1]

def main() -> None:
    pass


def unit_tests() -> None:
    print("unit tests starter her")
    assert tell_tegn("abc") == 3
    assert tell_tegn("abc. 5") == 6
    assert midt_tegn("abc") == "b"
    assert midt_tegn("abcd") == "bc"
    assert er_palindrom("Otto")
    assert er_palindrom("reker")
    assert er_palindrom("regninger")
    assert not er_palindrom("dom")
    print("alle unit tests passerte!")

if __name__ == "__main__":
    main()
    unit_tests()