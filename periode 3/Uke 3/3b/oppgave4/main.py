import os

import pandas as pd
from matplotlib import pyplot as plt

csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trafikkdata.csv")

df = pd.read_csv(csv_path, delimiter=";")

total_trafikk_indeks = df["Felt"] == "Totalt"

datapunkter = df[total_trafikk_indeks]

plt.grid(axis="y", alpha=0.8, zorder=0)
plt.bar(datapunkter["Fra tidspunkt"], datapunkter["Trafikkmengde"], zorder=3)
plt.xticks(rotation=45)
plt.title(f"Trafikkmengde per time")
plt.suptitle(f"Trafikk i {df['Navn'][0].title()}")
plt.show()
