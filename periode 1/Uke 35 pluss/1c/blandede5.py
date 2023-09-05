from collections import Counter
from string import ascii_letters

ascii_letters += "æøåÆØÅ"

tekst = "Finn en litt lang norsk tekst, for eksempel fra Wikipedia eller en nettavis, og finn antall forekomster av bokstavene a, e og k. Er bokstavene like vanlige? Tilpass programmet slik at du kan sjekke antall forekomster av alle bokstaver i det norske alfabetet. (Hint: Lag en tekst med det norske alfabetet som du går gjennom med en løkke. Sjekk deretter teksten din mot hver av bokstavene.) Hvilke bokstaver er vanligst?"

teller = Counter(tekst.lower())

for letter, count in teller.most_common():
    if letter in ascii_letters:
        print(f"bokstaven {letter} har {count} forekomster")
