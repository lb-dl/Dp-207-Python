MESSAGE_TO_CONTINUE = 'Would you like to continue? Enter "yes" or "y" to continue. Enter another button to stop. \n'
HELP_MSG = 'Height and width of a chess board must be integers greater than zero, e.g. "4". Try again, please. \n'
INSTRUCTIONS = 'To build a chessboard enter two integers: a height and a width of a chessboard, please. \n'
INPUT_MSG = 'Enter an integer, please. \n'


class Chess:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def chess_board(self):
        chess_board = [
            '* ' * self.width if i % 2 != 0
            else ' ' + '* ' * self.width for i in range(1, self.height + 1)]
        return chess_board


def validation(value):
    """
    The function checks and returns 'True' if the entered values are numbers greater than 0.
    Otherwise it prints a message with the further instructions and returns 'False'.
    """

    if isinstance(value, int) and value > 0:
        return True
    else:
        print(HELP_MSG)
        return False


def is_exit():
    """
    The function checks for the user input in order to continue (returns 'True')
    or quit a programme (returns 'False')
    """
    answer = input(MESSAGE_TO_CONTINUE)
    return answer.lower() in ['y', 'yes']


def get_user_input():

    # Ask users for input
    user_input = input(INPUT_MSG)
    return user_input


def main():
    print(INSTRUCTIONS)
    run = True
    while run:
        try:
            h = int(get_user_input())
            if validation(h):
                w = int(get_user_input())
                if validation(w):
                    chess = Chess(h, w)
                    for line in chess.chess_board():
                        print(line)
        except ValueError:
            print(HELP_MSG)
        run = is_exit()


if __name__ == '__main__':
    main()
