# from oppgave1 import
import os

import pandas as pd
from matplotlib import pyplot as plt


def get_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)


def subtask_a(data: pd.DataFrame) -> None:
    data.plot(
        xlabel="År #",
        ylabel="Antall minutter per dag",
        title="Minutter per dag brukt til ulike medier etter medietype og år",
    )
    plt.legend(bbox_to_anchor=(1, 1))
    plt.subplots_adjust(right=0.75)
    plt.savefig(get_path("out/2a.png"))


def subtask_b(data: pd.DataFrame) -> None:
    data[["Internett", "Hjemme-PC", "Bøker"]].plot(
        xlabel="År #",
        ylabel="Antall minutter per dag",
        title="Minutter per dag brukt til ulike medier etter medietype og år",
    )
    plt.legend(bbox_to_anchor=(1, 1))
    plt.subplots_adjust(right=0.75)
    plt.savefig(get_path("out/2b.png"))


def subtask_c(data: pd.DataFrame) -> None:
    idxmax = data.idxmax()
    idxmin = data.idxmin()

    print(
        f"Minst tid på internett er ved år {idxmin['Internett']} med {data['Internett'][idxmin['Internett']]} minutter per dag"
    )
    print(
        f"Mest tid på internett er ved år {idxmax['Internett']} med {data['Internett'][idxmax['Internett']]} minutter per dag"
    )


def main() -> None:
    data = pd.read_csv(
        get_path("datasett/Medier.csv"),
        delimiter=";",
        skiprows=2,
        index_col=0,
        na_values={".", ".."},
    )
    data.columns = [2010 + i for i in range(10)]

    # Sending in data.T because df.plot() assumes x-data as column
    # subtask_b(data.T) # Output is saved to out/2a.png
    # subtask_b(data.T)  # Output is saved to out/2b.png
    subtask_c(data.T)


if __name__ == "__main__":
    main()
