from .envelop import Envelop, compare_envelops


def test_compare_envelops():
    assert compare_envelops(5, 7, 8, 10)
