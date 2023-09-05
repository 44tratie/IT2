def main() -> None:
    tall = int(input("skriv et heltall: "))

    print("tallet ditt er et oddetall" if tall % 2 else "tallet ditt er et partall")


if __name__ == "__main__":
    main()
