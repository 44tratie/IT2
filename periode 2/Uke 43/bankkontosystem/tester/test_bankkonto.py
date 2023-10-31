from modeller.bankkontoer.bankkonto import Bankkonto
from modeller.person import Person


def test_bankkonto() -> None:
    person = Person("Tien", "Tran", "98765432", "+47")
    konto = Bankkonto(person, "1234.12.12345")
    konto.innskudd(1000)
    konto.innskudd(2000)
    konto.uttak(1500)
    konto.uttak(2500)
    print(konto)
