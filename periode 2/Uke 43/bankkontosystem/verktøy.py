def bruker_godkjennelse(melding: str = "") -> bool:
    while True:
        match input(melding).lower():
            case "ja":
                return True
            case "nei":
                return False
            case _:
                print("Du skrev noe ugyldig")
