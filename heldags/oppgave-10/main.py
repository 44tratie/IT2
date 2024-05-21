import pandas as pd
from matplotlib import pyplot as plt
from verktøy import hent_absolutt_bane, hent_måned


def print_total_per_type(df: pd.DataFrame):
    """Deloppgave a."""

    # Type kostnader som eksisterer i datasettet
    type_kostnader = set(df["Type"].values)

    for type_kostnad in type_kostnader:
        print(f"Total forbruk på {type_kostnad}: {df[df["Type"] == type_kostnad]["Beløp"].sum()}")


def print_total_per_måned(df: pd.DataFrame):
    """Deloppgave b."""

    # Månedene som eksisterer i datasettet
    måneder = set(df["Dato"].map(hent_måned).values)

    # Vi vil printe kronologisk, så vi legger til en sorted()
    for måned in sorted(måneder):
        print(f"Total forbruk i måned {måned}: {df[df["Dato"].map(hent_måned) == måned]["Beløp"].sum()}")


def lag_månedsutviklingsgraf(df: pd.DataFrame):
    """Deloppgave c."""

    # Månedene som eksisterer i datasettet
    måneder = set(df["Dato"].map(hent_måned).values)

    # Ønsker å se kostnadsutviklingen kronologisk
    x_verdier = sorted(måneder)
    y_verdier = []

    hverdagsutgifter = {"mat", "klær"}

    # Hent månedskostnad per måned
    for måned in x_verdier:
        riktig_måned = df[df["Dato"].map(hent_måned) == måned]
        y_verdier.append(riktig_måned[riktig_måned["Type"].isin(hverdagsutgifter)]["Beløp"].sum())

    # Opprett en graf
    fig, ax = plt.subplots()

    ax.plot(x_verdier, y_verdier)

    # Pynt grafen
    ax.set_xlabel("Måned")
    ax.set_ylabel("Totale kostnader")
    fig.suptitle("Månedsutvikling på utgiftene til familien Rosendal")

    # Lagre grafen
    fig.savefig(hent_absolutt_bane("10c.png"))
    

def lag_type_utgift_diagram(df: pd.DataFrame):
    """Deloppgave d."""

    # Definerer typer kostnader som type utgifter
    faste_utgifter = {"strøm"}
    hverdagsutgifter = {"mat", "klær"}

    # Hent utgiftenes kostnad
    faste_utgifter_sum = df[df["Type"].isin(faste_utgifter)]["Beløp"].sum()
    hverdagsutgifter_sum = df[df["Type"].isin(hverdagsutgifter)]["Beløp"].sum()

    # Lag en graf
    fig, ax = plt.subplots()

    # Legg til et søylediagram
    ax.bar(["Faste utgifter (strøm)", "Hverdagsutgifter (mat + klær)"], [faste_utgifter_sum, hverdagsutgifter_sum])
    
    # Pynt diagrammet
    ax.set_xlabel("Type utgift")
    ax.set_ylabel("Kostnadssum")
    fig.suptitle("Faste vs hverdagslige kostnader hos familien Rosendal")

    # Lagre diagrammet
    fig.savefig(hent_absolutt_bane("10d.png"))


def main() -> None:
    # Henter banen til csv filen og leser filen
    csv_bane = hent_absolutt_bane("utgifter.csv")
    df = pd.read_csv(csv_bane, delimiter=";", skiprows=1)
    # df["Dato"] = pd.to_datetime(df["Dato"], format="%d.%m.%Y")
    # print(df["Dato"][0].month)
    # print_total_per_type(df)
    # print_total_per_måned(df)
    lag_månedsutviklingsgraf(df)
    # lag_type_utgift_diagram(df)



if __name__ == "__main__":
    main()
