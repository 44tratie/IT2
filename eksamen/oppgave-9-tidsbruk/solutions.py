from typing import Literal

import numpy as np
import pandas as pd
from data_loading.duration import Duration
from matplotlib import pyplot as plt


def get_duration_minutes(duration: Duration) -> int:
    return duration.total_minutes()


def subtask_a(data: pd.DataFrame) -> pd.DataFrame:
    # In this task I assume that by "Aktivitet", we are talking about the various categories and NOT the summaries (denoted with "i alt"). That is the activities that are prefixed with a ¬ in the csv.

    print("Oppgave 9a")

    # Filter out the sub categories and retreieve the 3 relevant columns
    main_data = data[data["is_sub_category"] == True][
        ["sub_category", "sex", "time_spent"]
    ]
    # Rename column names to norwegian
    main_data.columns = ["Aktivitet", "Kjønn", "Tidsbruk"]
    # Print a table with only the three columns as described in the task statement
    print(main_data)
    print("--------------")

    # Also return the data for use in subtask b
    return main_data


def subtask_b(
    main_data: pd.DataFrame,
    sex_filter: Literal["Alle"] | Literal["Menn"] | Literal["Kvinner"],
) -> None:
    print("Oppgave 9b")

    filtered_data = main_data[main_data["Kjønn"] == sex_filter]

    # Print the filtered dataframe
    print(filtered_data.set_index("Aktivitet"))

    print("--------------")

    # Return the data for use in subtask c
    return filtered_data


def subtask_c(
    filtered_data: pd.DataFrame,
    sex_filter: Literal["Alle"] | Literal["Menn"] | Literal["Kvinner"],
) -> None:
    # I choose to split up this task into two tasks
    # subtask_c_1(filtered_data, sex_filter)
    subtask_c_2(filtered_data, sex_filter)


def subtask_c_1(
    filtered_data: pd.DataFrame,
    sex_filter: Literal["Alle"] | Literal["Menn"] | Literal["Kvinner"],
) -> None:
    fig, ax = plt.subplots()
    ax: plt.Axes  # Apply a type hint for an easier time programming

    # Makes evenly positioned positions for the bars
    positions = np.arange(len(filtered_data))

    # I choose to use horizontal bars because the labels are pretty long,
    # which could obstruct visibility on a normal verical bar chart
    # Since we have stored durations as objects, we can call the .total_minutes method on each duration
    ax.barh(
        positions,
        filtered_data["Tidsbruk"].map(get_duration_minutes),
    )

    # Set chart information
    ax.set_title(f"Tidsbruk i ulike aktiviteter for {sex_filter}")
    ax.set_yticks(positions, filtered_data["Aktivitet"])
    ax.set_xlabel("Antall minutter brukt")

    fig.tight_layout()
    fig.savefig("9c1.png")
    plt.show()


def subtask_c_2(
    filtered_data: pd.DataFrame,
    sex_filter: Literal["Alle"] | Literal["Menn"] | Literal["Kvinner"],
) -> None:
    fig, ax = plt.subplots()
    ax: plt.Axes

    ax.pie(
        filtered_data["Tidsbruk"].map(get_duration_minutes),
        labels=filtered_data["Aktivitet"],
        textprops={"size": "xx-small"},
        rotatelabels=True,
        # Text overlaps, better to not display percentages
        # autopct=r"%1.1f%%",
        # pctdistance=0.8,
    )

    fig.suptitle(f"Tidsbrukfordeling blant aktiviteter for {sex_filter}")

    fig.tight_layout()
    fig.savefig("9c2.png")
    plt.show()


def subtask_example(data: pd.DataFrame) -> None:
    print(data)
    a = lambda sex: data[
        (~data["is_sub_category"])
        & (data["sex"] == sex)
        & (data["main_category"] != "I alt")
    ]
    data_1 = a("Menn")
    data_2 = a("Kvinner")
    data_3 = a("Alle")

    ind = np.arange(len(data_1))
    width = 0.30

    fig, ax = plt.subplots()
    ax: plt.Axes

    bar1 = ax.barh(
        ind + width,
        data_1["time_spent"].map(lambda x: x.total_minutes()),
        width,
        label="Menn",
    )  # første bar-diagram
    bar2 = ax.barh(
        ind,
        data_2["time_spent"].map(lambda x: x.total_minutes()),
        width,
        label="Kvinner",
    )  # andre bar-diagram
    bar2 = ax.barh(
        ind - width,
        data_3["time_spent"].map(lambda x: x.total_minutes()),
        width,
        label="Alle",
    )  # andre bar-diagram

    ax.set_yticks(ind, data_1["main_category"])  # lager antall ticks som man har data
    ax.set_xlabel("Tid i minutter")
    ax.set_title("Tidsforbruk på diverse aktiviteter")
    ax.legend()
    fig.tight_layout()

    plt.show()
