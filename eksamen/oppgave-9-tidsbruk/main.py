import os

from data_loading import load_activity_data
from solutions import subtask_a, subtask_b, subtask_c, subtask_example


def main() -> None:
    """Entry point for this program"""

    data_abs_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        "data",
        "05994_20240126-145813-csv.csv",
    )

    df = load_activity_data(data_abs_path)

    SEX_FILTER = "Alle"

    main_df = subtask_a(df)
    filtered_main_df = subtask_b(main_df, SEX_FILTER)
    subtask_c(filtered_main_df, SEX_FILTER)


if __name__ == "__main__":
    main()
