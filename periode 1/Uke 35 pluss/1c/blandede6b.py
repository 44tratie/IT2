maks_forsøk = 10

fasit_tall = 404

forsøk = 1

while forsøk <= maks_forsøk:
    tall = int(input("gjett et heltall: "))

    if tall > fasit_tall:
        print("tallet er for stort")
    elif tall < fasit_tall:
        print("tallet er for lite")
    else:
        print("du gjettet svaret!")
        exit()
    forsøk += 1

print("du brukte for mange forsøk :(")
