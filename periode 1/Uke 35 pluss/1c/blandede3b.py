følge = []

while True:
    try:
        tall = float(input("skriv et tall: "))
        if tall > 10:
            break
        følge.append(tall)
    except ValueError:
        print("du skrev ikke et gyldig tall")

print(f"minste tall: {min(følge)}")
print(f"største tall: {max(følge)}")
print(f"summen av tallene: {sum(følge)}")
print(f"gjennomsnittet av tallene: {sum(følge) / len(følge)}")
