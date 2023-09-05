def main() -> None:
    tall = float(input("skriv en temperatur: "))
    enhet = input("skriv enhet (C eller F): ").lower()

    if enhet == "c":
        print(f"{tall}C = {tall * (9/5) + 32}F")
    elif enhet == "f":
        print(f"{tall}F = {(tall - 32) * (5/9)}C")
    else:
        raise ValueError("ugyldig enhet oppgitt")


if __name__ == "__main__":
    main()
