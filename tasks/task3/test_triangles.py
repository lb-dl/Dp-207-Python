import pytest
import mock
import builtins

from .triangles import *


@pytest.fixture
def triangles():
    triangle1 = Triangle('triangle1', 3.22, 2.96, 2.53)
    triangle2 = Triangle('triangle2', 26.8, 22.84, 29.64)
    return triangle1, triangle2


def test_sorted_list(triangles):
    expected_list = [292, 4]
    assert expected_list == sorted([triangles[0].get_area(), triangles[1].get_area()], reverse=True)


@pytest.fixture
def triangle():
    return Triangle('triangle1', 4.2, 5.1, 6.8)


def test_get_area(triangle):
    assert triangle.get_area()


def test_is_triangle(triangle):
    assert triangle.is_triangle()


def test_not_a_triangle():
    triangle = Triangle('triangle1', 4.2, 5.1, 167.8)
    assert triangle.is_triangle().__eq__(False)


@pytest.fixture
def input_data():
    with mock.patch.object(builtins, 'input', lambda _: 'triangle1, 4.3,5.2,five'):
        user_input = get_user_input()
        triangle_name = user_input[0]
        side_a = user_input[1]
        side_b = user_input[2]
        side_c = user_input[3]
    return triangle_name, side_a, side_b, side_c


def test_valid_data(input_data):
    assert input_data[1].__eq__(True)


def test_invalid_data(input_data):
    assert input_data[3].__eq__(False)


def test_user_answer_yes():
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        assert is_exit().__eq__(True)


def test_user_input():
    with mock.patch.object(builtins, 'input', lambda _: 'triangle1, 4.3,5.2,6.7'):
        assert get_user_input() == 'triangle1, 4.3,5.2,6.7'
