from datetime import datetime

from app import App
from bilkollektiv import BilKollektiv
from reserveringssystem import Reservasjon, Reserveringssystem


def gammel():
    """Et eksempel på hvordan en bruker kan legge til reservasjon i et reserveringssystem"""

    # Dependency injection: bilkollektivet varierer, f.eks. Oslo bilkollektiv vs Nordstrand bilkollektiv, derfor sender vi vårt bilkollektiv inn i systemet
    reserveringsssytem = Reserveringssystem(BilKollektiv(), simulasjon=True)

    reserveringsssytem.bilkollektiv.vis_biler()  # Brukeren ser at f.eks. EV73456 er i bilkollektivet

    # Inputhandling (f.eks sluttdato > startdato) gjøres når brukeren skriver inn verdiene, ikke ved opprettelsen av objektet
    # Gyldighet av reservasjon derimot, sjekkes ved opprettelse
    reservering_1 = Reservasjon(
        "Tien Tran",
        "44tratie@stud.akademiet.no",
        "EV73456",
        datetime(2024, 6, 10),
        datetime(2024, 6, 12),
    )
    reserveringsssytem.lag_reservasjon(reservering_1)

    # Brukeren angrer
    reserveringsssytem.fjern_reservasjon(reservering_1.reservasjon_ID)

    # Brukeren angrer igjen og lager en ny reservasjon
    reservering_2 = Reservasjon(
        "Tien Tran",
        "44tratie@stud.akademiet.no",
        "EV73456",
        datetime(2024, 6, 10),
        datetime(2024, 6, 12),
    )
    reserveringsssytem.lag_reservasjon(reservering_2)

    # Brukeren kjører og leverer etter 5 km
    reserveringsssytem.lever_bil(reservering_2, 5)  # Brukeren ser opplysningene

    # Bildata.json oppdateres automatisk (hvis simulasjon er False, som det skal være i produksjon)


def main() -> None:
    reserveringssystem = Reserveringssystem(BilKollektiv(), simulasjon=False)
    app = App(reserveringssystem)

    app.kjør()


if __name__ == "__main__":
    main()
