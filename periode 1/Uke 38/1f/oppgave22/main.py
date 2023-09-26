from gjennomsnitt import gjennomsnitt
from minst import minst
from størst import størst
from sum import summer


def main() -> None:
    print(gjennomsnitt([1, 2, 3, 4, 5]))
    print(minst([1, 2, 3, 4, 5]))
    print(størst([1, 2, 3, 4, 5]))
    print(summer([1, 2, 3, 4, 5]))



if __name__ == "__main__":
    main()