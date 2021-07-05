import unittest

from unittest.mock import patch

from ..task2.envelop import *


def test_first_envelop_is_bigger():
    e1 = Envelop(15, 17)
    e2 = Envelop(8, 10)
    assert e1.__lt__(e2)


def test_second_envelop__is_bigger():
    e1 = Envelop(5, 7)
    e2 = Envelop(8, 10)
    assert not e1.__lt__(e2)


def test_validation_positive_float_number():
    assert validation(4.2) is True


def test_validation_negative_number():
    """
    Test if the function "validation" returns True passing a positive integer as an argument
    """
    assert validation(-5) is False


def test_user_answer_yes():
    with unittest.mock.patch('builtins.input', return_value='y'):
        assert is_exit() is True


def test_user_input():
    with unittest.mock.patch('builtins.input', return_value='5,6'):
        assert get_user_input() == '5,6'
