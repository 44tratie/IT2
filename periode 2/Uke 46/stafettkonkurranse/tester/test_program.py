from modeller.gutt import Gutt
from modeller.idrettslag import Idrettslag
from modeller.jente import Jente
from modeller.stafettkonkurranse import Stafettkonkurranse


def test_program():
    gutter = [Gutt(navn) for navn in "ABCD"] + [Gutt("E", eksplisitt_løpetid=10000)]
    jenter = [Jente(navn) for navn in "fghi"] + [Jente("j", eksplisitt_løpetid=10000)]

    idrettslag = Idrettslag(gutter, jenter)

    (lag), rest = idrettslag.trekk_to_lag(antall_gutter=2, antall_jenter=2)
    dommere = rest[0:2]  # Vi ønsker å ha 2 dommere/arrangører

    konkurranse = Stafettkonkurranse(lag, dommere)

    print(konkurranse)

    resultater = konkurranse.gjør_løp()

    Stafettkonkurranse.print_vinner(resultater)
