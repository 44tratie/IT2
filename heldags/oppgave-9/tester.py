from veksle_penger import veksle_penger

def test_veksle_penger():
    assert veksle_penger(350) == {20: 17, 10: 1}
    assert veksle_penger(300) == {20: 15}
    assert veksle_penger(250) == {20: 12, 10: 1}
    assert veksle_penger(400) == {20: 20}
    assert veksle_penger(70) == {}