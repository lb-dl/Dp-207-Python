from .num_sequence import NaturalNumericSequence


def test_natural_number_sequence():
    n = NaturalNumericSequence(56)
    assert n.get_num_sequence()
