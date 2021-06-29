from .chess import Chess


def test_chess_board():
    expected_chess_board = ['* * ']
    chess = Chess(1, 2)
    result = chess.chess_board()
    assert expected_chess_board == result
