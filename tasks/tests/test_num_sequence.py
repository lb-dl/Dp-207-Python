from ..task7.num_sequence import *


def test_natural_number_sequence_valid_input():
    n = NaturalNumericSequence(67)
    assert n.get_num_sequence() == [1, 2, 3, 4, 5, 6, 7, 8]


def test_natural_number_sequence_zero():
    n = NaturalNumericSequence(0)
    assert n.get_num_sequence() == []


def test_natural_number_sequence_invalid_input():
    n = NaturalNumericSequence(-67)
    assert n.get_num_sequence() == []


def test_user_input(mocker):
    mocker.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(integer=100))
    res = get_number()
    assert res == 100
