from HSH7 import konverter_til_binær, skaff_heltall


def main() -> None:
    tall = skaff_heltall(1, 64)
    konvertert = konverter_til_binær(tall)
    print(f"{tall} (base-10) er {konvertert} (base-2)")


if __name__ == "__main__":
    main()
