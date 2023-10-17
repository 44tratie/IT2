tall = 123456789012340123012010
tall_str = str(tall)

# Dersom vi ønsker et arraybasert sluttsvar skraper vi ideen om Counter, og lager heller en comprehension:

frekvens_liste = [tall_str.count(siffer) for siffer in "0123456789"]

print(f"{frekvens_liste = }")
