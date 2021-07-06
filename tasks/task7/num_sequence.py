import argparse


INCORRECT_NUM_MSG = 'A positive integer should be entered'
MESSAGE = 'Would you like to continue? Enter "yes" or "y" to continue. Enter another button to stop \n'


class NaturalNumericSequence:

    def __init__(self, num):
        self.num = num

    def num_sequence(self):
        # The function yields a positive integer
        a = 1
        while a * a < self.num:
            yield a
            a += 1

    def get_num_sequence(self):

        numerical_sequence = [n for n in self.num_sequence()]
        return numerical_sequence


def get_number():
    """
    The function defines which arguments are required and parses them from a command-line.
    The help and usage messages are generated in case of entering incorrect data
    """

    parser = argparse.ArgumentParser(description='Get an integer')
    parser.add_argument('integer', type=int, help='A positive integer')
    args = parser.parse_args()
    num = args.integer
    return num


def main():

    number = get_number()
    if number == 0:
        return 0
    elif number < 0:
        print(INCORRECT_NUM_MSG)
        quit()
    n = NaturalNumericSequence(number)
    print(f'The sequence of integers which square is smaller than {number}: ')
    print(*n.get_num_sequence(), sep=', ')


if __name__ == '__main__':
    main()
