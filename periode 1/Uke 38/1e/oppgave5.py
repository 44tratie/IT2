top_populations = {
    "China": 1_413_142_846,
    "India": 1_399_179_585,
    "United States": 334_994_511,
    "Indonesia": 279_476_346,
    "Pakistan": 247_653_551,
}

print(f"Alle navnene er: {', '.join(top_populations.keys())}")

print(f"Alle innbyggertallene: {', '.join(map(str, top_populations.values()))}")

for country, population in top_populations.items():
    print(f"{country} har {population} innbyggere")

print(f"Landene i alfabetisk rekkefølge: {', '.join(sorted(top_populations.keys()))}")

country_with_lowest_population = min(top_populations, key=top_populations.get)
country_with_highest_population = max(top_populations, key=top_populations.get)
print(f"{country_with_highest_population} har flest innbyggere. {country_with_lowest_population} har færrest innbyggere.")