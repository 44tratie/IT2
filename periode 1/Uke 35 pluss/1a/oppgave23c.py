def minutter_til_timer(minutter: float) -> float:
    timer = minutter // 60
    gjenværende_minutter = timer % 60
    return timer, gjenværende_minutter

def main() -> None:
    print(minutter_til_timer(float(input("skriv et tall: "))))


if __name__ == "__main__":
    main()