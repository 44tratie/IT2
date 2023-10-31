from modeller.bankkontoer.bsu import BSU
from modeller.person import Person


def test_bsu() -> None:
    person = Person("Tien", "Tran", "98765432", "+47")
    konto = BSU(person, "1234", 27500)
    konto.innskudd(20000)
    konto.uttak(2500)
    konto.innskudd(9999)
    konto.innskudd(10)
    print(konto)
