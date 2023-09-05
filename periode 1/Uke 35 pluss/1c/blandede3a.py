maks_tall = int(input("skriv et heltall: "))

følge = range(1, maks_tall + 1)

print(
    f"summen av alle positive heltall opp til {maks_tall} er {sum(følge)}, og gjennomsnittet er {sum(følge) / maks_tall}"
)
