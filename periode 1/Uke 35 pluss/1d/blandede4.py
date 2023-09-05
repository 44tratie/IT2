import random

tall1 = [random.randint(0, 100) for _ in range(25)]
tall2 = [random.randint(0, 100) for _ in range(10)]


def median(følge):
    if len(følge) % 2:
        midt_indeks = len(følge) // 2
        return sorted(følge)[midt_indeks]

    sortert = sorted(følge)
    return (sortert[len(følge) // 2] + sortert[len(følge) // 2 - 1]) / 2


def main() -> None:
    print("medianen er:", median(tall1))
    print("medianen er:", median(tall2))


if __name__ == "__main__":
    main()
