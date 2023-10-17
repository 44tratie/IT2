from random import randint

min_verdi = 1
maks_verdi = 10
antall_tilfeldige_tall = 19

tilfeldige_tall = [
    randint(min_verdi, maks_verdi) for _ in range(antall_tilfeldige_tall)
]

print(f"{sum(tilfeldige_tall) = }")
