streng = "doingy boingy!!!!!"

teller: dict[str, int] = {}

for bokstav in streng:
    if bokstav not in teller:
        teller[bokstav] = 1
        continue
    
    teller[bokstav] += 1

print(teller)