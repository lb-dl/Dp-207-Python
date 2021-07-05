import pytest

from ..task5.num_to_words import *


def get_numbers():
    test_map = {0: 'ноль', 110: 'сто десять', 21049: 'двадцать одна тысяча сорок девять',
                93000: 'девяносто три тысячи', 612001: 'шестьсот двенадцать тысяч один',
                3000000: 'три миллиона', 211000000: 'двести одиннадцать миллионов',
                501000067: 'пятьсот один миллион шестьдесят семь',
                917552879: 'девятьсот семнадцать миллионов пятьсот пятьдесят две тысячи восемьсот семьдесят девять'}
    for key, val in test_map.items():
        yield key, val


@pytest.mark.parametrize("items", get_numbers())
def test_valid_num_to_words(items):
    key, val = items
    assert val == NumberToWords().number_to_words(key)


@pytest.fixture()
def num_to_words():
    return NumberToWords()


def test_to_words(num_to_words):
    assert 'сто тысяч восемьсот девяносто' == num_to_words.number_to_words(100890)


def test_get_digits(num_to_words):
    assert num_to_words.get_digits(100) == [0, 0, 1]


def test_user_input(mocker):
    mocker.patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(integer=100890))
    res = get_number()
    assert res == 100890


def test_too_big_number():
    """
    Test if number greater than 100.000.000 raises KeyError exception
    """
    with pytest.raises(KeyError):
        NumberToWords().number_to_words(10000000000000000)


def test_negative_number():
    """
    Test if negative number raises ValueError exception
    """
    with pytest.raises(ValueError):
        NumberToWords().number_to_words(-1)
