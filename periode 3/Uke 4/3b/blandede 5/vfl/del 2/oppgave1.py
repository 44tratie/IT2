import os

import numpy as np
from matplotlib import pyplot as plt


def get_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


def load_csv(path: str, skip_rows: int = 2) -> list[str]:
    with open(path, encoding="utf-8") as csv_file:
        lines = csv_file.readlines()

    return lines[skip_rows:]


def convert_item(string: str) -> int | float:
    if string in {".", ".."}:
        return np.NaN

    return int(string)


def prepare_data(raw_data: list[str]):
    # Remove stuff like "Minutter brukt til ulike medier en gjennomsnittsdag"
    headers = []

    # Iterates over each header with ""s removed and split by ;
    for header in map(
        lambda header: header.strip('"'), raw_data[0].strip().split(";")[1:]
    ):
        # The year is located as the last word in each header
        headers.append(header.split()[-1])

    # I choose to save datarows in a dictionary
    data = {}

    # Splits a row into string lists of the rowdata and iterates over the rows
    for row in map(lambda row: row.strip().split(";"), raw_data[1:]):
        # Becomes data["Papiravis"] (not data[""Papiravis""]) = [23, 24, NaN, ...]
        data[row[0].strip('"')] = list(map(convert_item, row[1:]))

    return data, headers


def subtask_a(data: dict[str, list[int | float]], headers: list[str]) -> None:
    for key in data:
        plt.plot(headers, data[key], label=key)

    plt.legend(loc="upper right")
    plt.ylabel("Antall minutter per dag")
    plt.xlabel("År #")
    plt.title("Minutter per dag brukt til ulike medier etter medietype og år")
    plt.savefig(get_path("out/1a.png"))


def subtask_b(data: dict[str, list[int | float]], headers: list[str]) -> None:
    # Filters the data by the provided keys
    for key in filter(lambda key: key in {"Internett", "Hjemme-PC", "Bøker"}, data):
        plt.plot(headers, data[key], label=key)

    plt.legend(loc="upper right")
    plt.ylabel("Antall minutter per dag")
    plt.xlabel("År #")
    plt.title("Minutter per dag brukt til ulike medier etter medietype og år")
    plt.savefig(get_path("out/1b.png"))


def subtask_c(data: dict[str, list[int | float]], headers: list[str]):
    # Algotithm to find minimum and maximum value and their associated index
    # (value, index)
    min = (np.inf, None)
    max = (0, None)
    for i, val in enumerate(data["Internett"]):
        if val < min[0]:
            min = (val, i)

        if val > max[0]:
            max = (val, i)

    print(
        f"Minst tid på internett er ved år {headers[min[1]]} med {min[0]} minutter per dag"
    )
    print(
        f"Mest tid på internett er ved år {headers[max[1]]} med {max[0]} minutter per dag"
    )


def main() -> None:
    data = load_csv(get_path("datasett\Medier.csv"))

    data, headers = prepare_data(data)

    # subtask_a(data, headers) # Output is saved to out/1a.png
    # subtask_b(data, headers) # Output is saved to out/1b.png
    subtask_c(data, headers)


if __name__ == "__main__":
    main()
