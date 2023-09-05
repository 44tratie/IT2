maaneder = "JanFebMarAprMaiJunJulAugSepOktNovDes"

maanedstall = int(input("skriv et månedstall: "))


def tall_til_indeks(tall: int) -> slice:
    return slice(3 * (tall - 1), 3 * tall)


print(maaneder[tall_til_indeks(maanedstall)])
