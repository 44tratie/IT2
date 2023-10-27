from modeller.bankkonto import Bankkonto


def test_bankkonto() -> None:
    konto = Bankkonto("Tien Tran", "1234.12.12345")
    konto.innskudd(1000)
    konto.innskudd(2000)
    konto.uttak(1500)
    konto.uttak(2500)
    print(konto)
