import pytest
import unittest
from unittest.mock import patch, Mock

from ..task3.triangles import *


@pytest.fixture
def triangles():
    triangle1 = Triangle('triangle1', 3.22, 2.96, 2.53)
    triangle2 = Triangle('triangle2', 26.8, 22.84, 29.64)
    return triangle1, triangle2


def test_sorted_list(triangles):
    expected_list = [292.42, 3.55]
    assert expected_list == sorted([triangles[0].get_area(), triangles[1].get_area()], reverse=True)


@pytest.fixture
def triangle():
    return Triangle('triangle1', 4.2, 5.1, 6.8)


def test_get_area(triangle):
    assert triangle.get_area() == 10.69


def test_get_area_invalid_result(triangle):
    assert triangle.get_area() != 11


def test_is_triangle(triangle):
    assert triangle.is_triangle() is True


def test_not_a_triangle():
    triangle = Triangle('triangle1', 4.2, 5.1, 167.8)
    assert triangle.is_triangle() is False


def test_user_answer_yes():
    with unittest.mock.patch('builtins.input', return_value='y'):
        assert is_exit() is True


def test_user_input():
    with unittest.mock.patch('builtins.input', return_value='triangle1, 4.3,5.2,6.7'):
        assert get_user_input() == 'triangle1, 4.3,5.2,6.7'


def test_sort_triangles():
    test_list_of_triangles = [['tr1', 11.18], ['tr2', 9.12], ['tr3', 292.42], ['tr4', 3.55]]
    assert sort_triangles(test_list_of_triangles) == []