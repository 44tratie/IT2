import numpy as np

Array = np.ndarray[np.integer | np.floating]


def double(arr: Array) -> Array:
    return arr * 2


def main() -> None:
    opprinnelig_array = np.array([1, 3, 5, 8])
    dobbelt_array = double(opprinnelig_array)

    print(f"{opprinnelig_array = }\n{dobbelt_array = }")


if __name__ == "__main__":
    main()
