import os

import numpy as np
import pandas as pd

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")

df = pd.read_json(path).set_index("id")

# print(df)


def subtask_b():
    print("Alle oppgaver")
    for id, row in df.iterrows():
        print(
            f"({'Ferdig' if row['completed'] else 'Uferdig'})\tOppgave {id} (Bruker {row['userId']})\t- {row['title']}"
        )


def subtask_c():
    print("Ufullførte oppgaver")
    is_completed = df["completed"] == True
    for id, row in df[np.invert(is_completed)].iterrows():
        print(f"Oppgave {id} (Bruker {row['userId']})\t- {row['title']}")

    print("Fullførte oppgaver")
    for id, row in df[is_completed].iterrows():
        print(f"Oppgave {id} (Bruker {row['userId']})\t- {row['title']}")


def subtask_d():
    is_completed = df["completed"] == True
    counts = df[is_completed].value_counts(["userId"])
    hardt_arbeidende_arbeider = counts.idxmax()[0]
    print(
        f"Bruker {hardt_arbeidende_arbeider} jobbet mest med {counts[hardt_arbeidende_arbeider]} oppgaver"
    )


def subtask_e():
    is_completed = df["completed"] == True
    counts = df[is_completed].value_counts(["userId"])
    lokende_arbeider = counts.idxmin()[0]
    print(
        f"Bruker {lokende_arbeider} jobbet minst med {counts[lokende_arbeider]} oppgaver"
    )


def main() -> None:
    subtask_b()
    print()
    subtask_c()
    print()
    subtask_d()
    print()
    subtask_e()


if __name__ == "__main__":
    main()
