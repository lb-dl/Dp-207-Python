class Chess:
    help = 'Height and weight of a chess board must be integers, e.g. "4" '

    def __init__(self, h, w):
        self.h = h
        self.w = w

    def chess_board(self):
        for i in range(1, self.h+1):
            if i % 2 != 0:
                print('* ' * self.w)
            else:
                print(' ' + '* ' * self.w)


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
        chess.chess_board()
    except ValueError:
        print(Chess.help)
