from modeller.sparekonto import Sparekonto


def test_sparekonto() -> None:
    konto = Sparekonto("Tien Tran", "1234,", 3, start_saldo=1000)
    konto.uttak(333)
    konto.uttak(333)
    konto.uttak(333)
    konto.uttak(1)
    konto._reset_antall_uttak()
    konto.uttak(1)
    konto.innskudd(1000)
    konto.uttak(1000)
    konto.uttak(1)
    konto.innskudd(1)
    konto.uttak(1)
    konto.uttak(1)
    print(konto)
