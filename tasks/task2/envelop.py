from math import sqrt

INSTRUCTIONS = 'Enter a width, height of the envelop, separated by a comma "," (e.g. "5,6")'
HELP_MSG = 'The width and height must be numbers greater than 0, separated by commas, e.g. "5,6". Try again, please'
YES_SECOND_ENVELOP = 'It is possible to fit second envelop into first envelop'
YES_FIRST_ENVELOP = 'It is possible to fit first envelop into second envelop'
NO_ANSWER = 'It is not possible to fit one envelop into another envelop'
MESSAGE = 'Would you like to continue? Enter "yes" or "y" to continue. Enter another button to stop'


def main():
    """
    The function asks a user to enter four numbers (width and height) for two envelops.
    If the entered values are valid it creates two class objects and calls the function
    'compare_envelops' to make a decision if it is possible to fit one envelop into another one.
    """

    run = True
    while run:
        try:
            print(INSTRUCTIONS)
            width1, height1 = [float(x) if validation(float(x)) else print(HELP_MSG) for x in input().split(',')]
            print(INSTRUCTIONS)
            width2, height2 = [float(x) if validation(float(x)) else print(HELP_MSG) for x in input().split(',')]
            e1 = Envelop(height1, width1)
            e2 = Envelop(height2, width2)
            if e1 > e2:
                print(YES_SECOND_ENVELOP)
            elif e2 > e1:
                print(YES_FIRST_ENVELOP)
            else:
                print(NO_ANSWER)
        except ValueError:
            print(HELP_MSG)
        run = is_exit()



def user_answer(string):
    """
    The function checks if a string is 'y' or 'yes'
    """

    if string.lower() in ['y', 'yes']:
        return True
    else:
        return False


def validation(value):
    """
    The function checks and returns 'True' if the entered values are numbers greater than 0.
    Otherwise it prints a message with the further instructions and returns 'False'.
    """

    if isinstance(value, float) and value > 0:
        return True
    else:
        print(HELP_MSG)
        return False


def is_exit():
    """
    The function checks for the user input in order to continue (returns 'True')
    or quit a programme (returns 'False')
    """
    answer = input(f'Would you like to continue?')
    if answer.lower() in ['y', 'yes']:
        return True
    else:
        return False


class Envelop:
    """ A class Envelop """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __lt__(self, other) -> bool:
        return (self.width > other.width and self.height > other.height) or \
                (self.width < other.width and self.height < other.height)


if __name__ == '__main__':
    main()
