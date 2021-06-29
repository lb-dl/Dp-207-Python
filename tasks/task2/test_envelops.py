from .envelop import Envelop


def test_compare_envelops():
    e1 = Envelop(5, 7)
    e2 = Envelop(8, 10)
    assert e1 > e2
