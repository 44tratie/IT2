import os

import pandas as pd


def parse_installs(installs_str: str) -> int:
    if installs_str[-1] != "+":
        return int(installs_str.replace(",", ""))

    return int(installs_str[:-1].replace(",", ""))


def subtask_a(df: pd.DataFrame) -> None:
    for index, count in df["Category"].value_counts()[:3].items():
        filtered = df[df["Category"] == index]
        installs = filtered["Installs"].apply(parse_installs)

        print(f"Kategori: {index.title()} ({count} apper)")
        print(f"Gjennomsnittlig nedlastninger: {round(installs.mean())}")
        print(f"Gjennomsnittlig rating: {round(filtered['Rating'].mean(), 2)}")
        print("")


def subtask_b(df: pd.DataFrame) -> None:
    for index, count in df["Category"].value_counts()[:3].items():
        filtered = df[df["Category"] == index]
        filtered["Installs"] = filtered["Installs"].map(parse_installs)
        filtered.sort_values("Installs", ascending=False, inplace=True)

        print(f"Kategori: {index.title()} ({count} apper)")
        print(f"Gjennomsnittlig nedlastninger: {round(filtered['Installs'].mean())}")
        print(f"Gjennomsnittlig rating: {round(filtered['Rating'].mean(), 2)}")
        print(f"De 3 mest populære apper innen kategorien {index.title()}:")
        for i in range(3):
            print(
                f"\t{filtered.iloc[i]['App']} ({filtered.iloc[i]['Installs']} nedlastninger)"
            )
        print("")


def main() -> None:
    df = pd.read_csv(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "googleplaystore.csv")
    )

    # Fjern feil funnet i datasett
    df.drop(10472, inplace=True)
    df.drop_duplicates("App", inplace=True)

    # subtask_a(df)
    subtask_b(df)


if __name__ == "__main__":
    main()
