# rip namespace
# from math import *

# clean
# from math import pi

# også good
# import math as m
# pi = m.pi

# good
import math

pi = math.pi


def omkrets(radius: float) -> float:
    return pi * 2 * radius


def areal(radius: float) -> float:
    return pi * radius**2


def main() -> None:
    print(f"r = 3: A = {areal(3)}, O = {omkrets(3)}")
    print(f"r = 12: A = {areal(12)}, O = {omkrets(12)}")
    print(f"r = 42: A = {areal(42)}, O = {omkrets(42)}")


if __name__ == "__main__":
    main()
