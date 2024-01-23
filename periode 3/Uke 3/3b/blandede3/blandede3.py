import os

import numpy as np
import pandas as pd
from matplotlib import colors as mcolors
from matplotlib import pyplot as plt

csv_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "fritidsboliger_moh_2019.csv"
)

df = pd.read_csv(csv_path, delimiter=";", index_col=0, header=None).T

over_1000m_index = [
    int(label.split("-")[0]) >= 1000 for label in df["Meter over havet"]
]

over_1000m = pd.DataFrame(
    data={
        "Meter over havet": "Over 1000 m",
        "Fritidsbygg": sum(df[over_1000m_index]["Fritidsbygg"].astype(int)),
    },
    index=[over_1000m_index.count(False) + 1],
)

ny_df = pd.concat([df[: over_1000m_index.count(False)], over_1000m])

rvb = plt.cm.Spectral_r

plt.barh(
    ny_df["Meter over havet"],
    ny_df["Fritidsbygg"].astype(int),
    color=rvb(np.arange(len(ny_df)).astype(float) / len(ny_df)),
)
plt.title("Antall hytter på visse høyder")
plt.xlabel("Antall hytter")
plt.ylabel("Høyden på hyttene")
plt.xticks(rotation=20)
plt.subplots_adjust(left=0.2, bottom=0.2)
plt.show()
