import json
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skandinavia.json")

with open(path, encoding="utf-8") as fil:
    data = json.load(fil)

print("Alle land i datasettet:")
for land in data["land"]:
    print(land["navn"])

print("\nByene i danmark:")
danmark = next(filter(lambda land: land["navn"] == "Danmark", data["land"]))
for by in danmark["byer"]:
    print(by)

print("\nAlle byene i hvert land:")
for land in data["land"]:
    print(f"Byer i {land['navn']}:")
    for by in land["byer"]:
        print(by)

print("\nAlle byene i Danmark som starter på A")
danmark = next(filter(lambda land: land["navn"] == "Danmark", data["land"]))
byer_med_a = filter(lambda by: by and by[0].lower() == "a", danmark["byer"])
for by in byer_med_a:
    print(by)
