class AgeError(ValueError):
    pass


while True:
    try:
        alder = int(input("skriv alderen din: "))
        if alder < 0:
            raise AgeError
        break
    except AgeError:
        print("du kan ikke være yngre enn 0")
    except ValueError:
        print("du skrev ikke et tall")

print("du er", alder, "år gammel")
