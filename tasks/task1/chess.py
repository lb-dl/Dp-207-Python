class Chess:
    help = 'Height and weight of a chess board must be integers greater than zero, e.g. "4" '

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def chess_board(self):
        chess_board = [
            '* ' * self.width if i % 2 != 0
            else ' ' + '* ' * self.width for i in range(1, self.height + 1)]
        return chess_board


if __name__ == '__main__':
    try:
        print('Enter a height of a chess board, please. It must be an integer ' + '\n')
        h = int(input())
        print('Enter a width of a chess board, please. It must be an integer ' + '\n')
        w = int(input())
        if not h and w:
            print(Chess.help)
        elif not isinstance(h, int) and not isinstance(w, int):
            print(Chess.help)
        chess = Chess(h, w)
        for line in chess.chess_board():
            print(line)
    except ValueError:
        print(Chess.help)
