from string import ascii_lowercase

# koden fungerer bare for lowercase dessverre :(

ascii_lowercase += "æøå"
letters = set(ascii_lowercase)

krypter = {
    letter: shifted_letter
    for letter, shifted_letter in zip(
        ascii_lowercase,
        ascii_lowercase[2:] + ascii_lowercase[:2]
    )
}

dekrypter = {
    shifted_letter: letter
    for letter, shifted_letter in zip(
        ascii_lowercase,
        ascii_lowercase[2:] + ascii_lowercase[:2]
    )
}

tekst_til_kryptering = "hei dette er en tekst"

kryptert = ""
for letter in tekst_til_kryptering:
    if letter not in letters:
        kryptert += letter
        continue
    kryptert += krypter[letter]

print(f"den krypterte teksten er: {kryptert}")

dekryptert = ""
for letter in kryptert:
    if letter not in letters:
        dekryptert += letter
        continue
    dekryptert += dekrypter[letter]


print(f"den dekrypterte teksten er: {dekryptert}")
