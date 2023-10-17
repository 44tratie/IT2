from random import randint

min_verdi = 1
maks_verdi = 100
antall_tilfeldige_tall = 10

tilfeldige_tall = [
    randint(min_verdi, maks_verdi) for _ in range(antall_tilfeldige_tall)
]

print(f"{tilfeldige_tall = }")

# Tuple er bedre i denne sammenhengen, siden disse tallene ikke skal endres på (for det meste)
tall_minmax = (min(tilfeldige_tall), max(tilfeldige_tall))

print(f"{tall_minmax = }")
