import pytest

from .triangles import Triangle


@pytest.fixture
def triangles():
    return Triangle('triangle1', 4, 5, 6)


def test_get_area(triangles):
    assert triangles.get_area()


def test_is_triangle(triangles):
    assert triangles.is_triangle()
