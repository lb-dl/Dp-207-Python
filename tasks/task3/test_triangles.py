import pytest
import mock
import builtins

from .triangles import *


@pytest.fixture
def triangles():
    return Triangle('triangle1', 4.2, 5.1, 6.8)


def test_get_area(triangles):
    assert triangles.get_area()


def test_is_triangle(triangles):
    assert triangles.is_triangle()


def test_validation():
    expected_res = validation(4.2)
    assert expected_res == True


def test_user_answer_yes():
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert is_exit() == True


def test_user_input():
    with mock.patch.object(builtins, 'input', lambda _: 'triangle1, 4.3,5.2,6.7'):
        assert get_user_input() == 'triangle1, 4.3,5.2,6.7'
