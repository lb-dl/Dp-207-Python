from ..task8.fibonacci import *
import pytest


def test_fibonacci_list():
    f = FibonacciSequence(8, 259)
    assert f.fib_list() == [8, 13, 21, 34, 55, 89, 144, 233]


def test_fib_list_num1_greater_num2():
    f = FibonacciSequence(259, 8)
    assert f.fib_list() == []


def test_user_input(mocker):
    mocker.patch('argparse.ArgumentParser.parse_args',
                 return_value=argparse.Namespace(integer1=100, integer2=200))
    res = get_numbers()
    assert res == (100, 200)


def test_get_index():
    f = FibonacciSequence
    test_list = [8, 13, 21, 34, 55, 89, 144, 233]
    assert f.get_index(test_list, 21) == 2


def test_get_fib_sequence():
    f = FibonacciSequence(0, 259)
    assert len(f.get_fib_sequence()) == 14


def test_negative_number():
    """
    Test if negative numbers raise ValueError exception
    """
    with pytest.raises(ValueError):
        FibonacciSequence(-3,-5).fib_list()


def invalid_output():
    f = FibonacciSequence(1, 5)
    assert f.fib_list() != [1, 9999, 2, 3]
