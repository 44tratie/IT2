while True:
    try:
        maanednr = int(input("Oppgi nummeret til måneden vi er i "))
        break
    except ValueError:
        print("ugyldig tall")

if maanednr >= 1 and maanednr <= 12:
    print(f"Du skrev inn {maanednr}.")
else:
    print("Du må oppgi et tall mellom 1 og 12.")
