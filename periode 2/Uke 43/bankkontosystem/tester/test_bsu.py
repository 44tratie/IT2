from modeller.bsu import BSU


def test_bsu() -> None:
    konto = BSU("Tien Tran", "1234", 27500)
    konto.innskudd(20000)
    konto.uttak(2500)
    konto.innskudd(9999)
    konto.innskudd(10)
    print(konto)
