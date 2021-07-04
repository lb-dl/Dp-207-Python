import pytest

from .num_to_words import *


@pytest.fixture()
def num_to_words():
    return NumberToWords(100890)


def test_get_digits(num_to_words):
    assert num_to_words.get_digits(100)


def test_user_input(mocker):
    mocker.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(integer=100890))
    res = get_number()
    assert res == 100890


def numbers():
    yield from [0, 110, 21049, 93000, 612001, 3000000, 211000000, 501000067, 917552879]


@pytest.mark.parametrize("number", numbers())
def test_num_to_words(number):
    assert NumberToWords().number_to_words(number)


