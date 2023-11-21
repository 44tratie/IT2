from modeller.person import Person


def test_person():
    navn = "Test Navn"

    person = Person(navn)

    assert str(person) == navn, "feil i __str__ metoden"

    for _ in range(1_000):
        assert (
            person._min_tid <= person.løp() <= person._maks_tid
        ), "person løp raskere eller tregere enn lovlig"

    løpetid = 15000
    person = Person(navn, eksplisitt_løpetid=løpetid)

    for _ in range(1_000):
        assert (
            person.løp() == løpetid
        ), f"person løp ikke {løpetid / 1000} sekunder når han burde det"
