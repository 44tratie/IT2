from klasser.kalkulator import Kalkulator


def test_pluss() -> None:
    assert Kalkulator.pluss(1, 2.5) == 3.5
    assert Kalkulator.pluss(1, -2) == -1
    assert Kalkulator.pluss(1.8, 2.6) == 4.4


def test_minus() -> None:
    assert Kalkulator.minus(1, 2.5) == -1.5
    assert Kalkulator.minus(1, -2) == 3
    assert Kalkulator.minus(1.8, 2.6) == -0.8


def test_gange() -> None:
    assert Kalkulator.gange(1, 2.5) == 2.5
    assert Kalkulator.gange(1, -2) == -2
    # Sjekker om point precision errors kan skje
    assert Kalkulator.gange(1.8, 2.6) == 4.68


def test_dele() -> None:
    assert Kalkulator.dele(1, 2.5) == 0.4
    assert Kalkulator.dele(1, -2) == -0.5
    try:
        assert Kalkulator.dele(1.8, 0) == None
    except ZeroDivisionError:
        raise Exception("Programmet håndterer ikke nulldivisjon")
