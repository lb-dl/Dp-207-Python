from .envelop import *
import mock
import builtins
import pytest


def test_first_envelop_bigger():
    e1 = Envelop(15, 17)
    e2 = Envelop(8, 10)
    assert e1.__lt__(e2)


def test_second_envelop_bigger():
    e1 = Envelop(5, 7)
    e2 = Envelop(8, 10)
    assert not e1.__lt__(e2)


def test_validation():
    expected_res = validation(4.2)
    assert expected_res.__eq__(True)


def test_user_answer_yes():
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert is_exit().__eq__(True)


def test_user_input():
    with mock.patch.object(builtins, 'input', lambda _: '5,6'):
        assert get_user_input() == '5,6'


@pytest.fixture
def input_valid_data():
    with mock.patch.object(builtins, 'input', lambda _: '5, 6'):
        user_input = get_user_input()
        width = user_input[0]
        height = user_input[1]
    return width, height


def test_valid_data(input_valid_data):
    assert input_valid_data[0].__eq__(True)
    assert input_valid_data[1].__eq__(True)


@pytest.fixture
def input_invalid_data():
    with mock.patch.object(builtins, 'input', lambda _: 'five, -6'):
        user_input = get_user_input()
        width = user_input[0]
        height = user_input[1]
    return width, height


def test_invalid_data(input_invalid_data):
    assert input_invalid_data[0].__eq__(False)
    assert input_invalid_data[1].__eq__(False)
