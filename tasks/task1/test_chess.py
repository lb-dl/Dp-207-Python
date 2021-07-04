from .chess import *
import pytest
import mock
import builtins


def test_valid_chess_board():
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
    with mock.patch.object(builtins, 'input', lambda _: '4'):
        assert get_user_input() == '4'
