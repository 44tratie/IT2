from modeller.bankkontoer.kredittkonto import Kredittkonto
from modeller.person import Person


def test_kredittkonto() -> None:
    person = Person("Tien", "Tran", "98765432", "+47")
    konto = Kredittkonto(person, "1234")

    konto.innskudd(1000)
    konto.innskudd(2000)
    konto.uttak(5000)
    konto.uttak(4000)
    print(konto)
