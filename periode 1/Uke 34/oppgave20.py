a = "100 m"
b = "300 000 km/s"
c = "2,718 281 828 459 045"


def remove_unit(string: str) -> str:
    number = ""
    has_decimal = False
    for letter in string:
        if letter == ",":
            if has_decimal:
                raise ValueError("bro tallet ditt har flere desimaltegn")
            has_decimal = True
            number += "."
            continue
        elif letter == " ":
            continue
        if letter.isdigit():
            number += letter
        else:
            return number
    return number


def convert(tall: str) -> int | float:
    if "." in tall:
        return float(tall)
    else:
        return int(tall)


def main() -> None:
    print(convert(remove_unit(a)))
    print(convert(remove_unit(b)))
    print(convert(remove_unit(c)))


if __name__ == "__main__":
    main()
