class SnittError(ValueError):
    pass


while True:
    try:
        snitt = float(input("skriv snittet (fra førstegangsvitnemål) ditt: "))

        if not 1 <= snitt <= 6.4:
            raise SnittError

        break
    except SnittError:
        print("snittet ditt er for høyt eller lavt enn menneskelig mulig")
    except ValueError:
        print("du skrev ikke et gyldig tall")

print("snittet ditt er", snitt)
