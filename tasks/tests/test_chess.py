import unittest
import pytest
from unittest.mock import patch
from ..task1.chess import *


def test_valid_chess_board():
    """
    Test if a chessboard 1x2 is printed (* *)
    """
    expected_chess_board = ['* * ']
    chess = Chess(1, 2)
    result = chess.chess_board()
    assert expected_chess_board == result


def test_invalid_chessboard():
    invalid_chess_board = [' * *']
    chess = Chess(1, 2)
    result = chess.chess_board()
    assert invalid_chess_board != result


def test_user_input():
    """
    Test the users input
    """
    with unittest.mock.patch('builtins.input', return_value='4'):
        assert get_user_input() == '4'


def test_invalid_data():
    """
    Test if str raises TypeError exception
    """
    with pytest.raises(TypeError):
        chess = Chess('y', 2)
        chess.chess_board()


def test_validation_positive_integer():
    """
    Test if the function "validation" returns True passing a positive integer as an argument
    """
    assert validation(5) is True


def test_validation_negative_integer():
    """
    Test if the function "validation" returns True passing a positive integer as an argument
    """
    assert validation(-5) is False
