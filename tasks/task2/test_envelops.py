from .envelop import *
import mock
import builtins


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
    assert expected_res == True


def test_user_answer_yes():
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert is_exit() == True


def test_user_input():
    with mock.patch.object(builtins, 'input', lambda _: '5,6'):
        assert get_user_input() == '5,6'
