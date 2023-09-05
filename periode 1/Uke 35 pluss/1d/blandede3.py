tall = []
har_sett = set()

while len(tall) < 10:
    ny_tall = int(input("skriv et heltall: "))

    if ny_tall not in har_sett:
        tall.append(ny_tall)
        har_sett.add(ny_tall)
    else:
        print("du har allerede skrevet inn tallet")

print(tall)
