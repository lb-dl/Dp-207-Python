import pytest

from .num_to_words import NumberToWords


@pytest.fixture()
def num_to_words():
    return NumberToWords(100890)


def test_get_digits(num_to_words):
    assert num_to_words.get_digits(100)


def test_number_to_words(num_to_words):
    assert num_to_words.number_to_words(100890)
