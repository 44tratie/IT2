from modeller.bankkontoer.sparekonto import Sparekonto
from modeller.person import Person


def test_sparekonto() -> None:
    person = Person("Tien", "Tran", "98765432", "+47")
    konto = Sparekonto(person, "1234,", 3, start_saldo=1000)
    konto.uttak(333)
    konto.uttak(333)
    konto.uttak(333)
    konto.uttak(1)
    konto.reset_antall_uttak()
    konto.uttak(1)
    konto.innskudd(1000)
    konto.uttak(1000)
    konto.uttak(1)
    konto.innskudd(1)
    konto.uttak(1)
    konto.uttak(1)
    print(konto)
