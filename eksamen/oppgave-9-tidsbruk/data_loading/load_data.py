import csv
from collections import defaultdict

import pandas as pd

from .duration import Duration


def load_activity_data(csv_path: str) -> pd.DataFrame:
    """Loads activity data given as preparation material for the spring 2024 REA3049 exam

    Parameters
    ----------
    path : str
        Path to the csv_file

    Returns
    -------
    pd.DataFrame
        A dataframe containing the data in the csv file as well as additional info such as hierarchy (main/sub-category).
    """

    # the data has "¬", which is included in the "iso-8859-1" charset
    with open(csv_path, encoding="iso-8859-1") as data_file:
        # Skip the first two lines containing table info
        data_file.readline()
        data_file.readline()

        data_reader = csv.DictReader(data_file, delimiter=";")

        # Reshape the data so that we can forward fill the main category to sub-categories
        reshaped_data = defaultdict(list)

        for data_point in data_reader:
            category = data_point["alle aktiviteter"]
            is_sub_category = category[0] == "¬"

            reshaped_data["main_category"].append(None if is_sub_category else category)
            reshaped_data["sub_category"].append(
                category.strip("¬ ") if is_sub_category else None
            )  # strip "¬" and whitespaces in front and back of category name
            reshaped_data["sex"].append(data_point["kjønn"])
            reshaped_data["time_spent"].append(
                Duration.from_string(data_point["Tidsbruk 2000 I alt"])
            )
            reshaped_data["is_sub_category"].append(is_sub_category)

    df = pd.DataFrame(reshaped_data)
    # Give sub_categories a pointer to the main_category by forward filling
    df["main_category"] = df["main_category"].ffill()

    return df
