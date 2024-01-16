import os

import pandas as pd
from matplotlib import pyplot as plt

csv_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "fritidsboliger_moh_2019.csv"
)

df = pd.read_csv(csv_path, delimiter=";", index_col=0, header=None).T

over_1000m = pd.DataFrame(
    data={
        "Meter over havet": "Over 1000 m",
        "Fritidsbygg": sum(df.iloc[13:]["Fritidsbygg"].astype(int)),
    },
    index=[14],
)

ny_df = pd.concat([df[:13], over_1000m])

plt.barh(ny_df["Meter over havet"], ny_df["Fritidsbygg"].astype(int))
plt.subplots_adjust(left=0.2)
plt.show()
