import argparse
import itertools


INCORRECT_NUM_MSG = 'Incorrect value'
FILE_NOT_FOUND_MSG = 'File not found'
MOSKOW = 'Moskow'
PITER = 'Piter'


def get_path():
    """
    The function defines which argument is required and parses it from a command-line.
    The help and usage messages are generated in case of entering incorrect data
    """
    parser = argparse.ArgumentParser(description='Path to a file')
    parser.add_argument('file_path', type=str, help='A pass to the file')
    args = parser.parse_args()
    file_path = args.file_path
    return file_path


def read_file(path):
    """
    The function gets a path to the file, then opens and reads the file.
    If there's a word 'Moskow' or 'Piter' in the file, the function
    returns 'Moskow' or 'Piter' respectively.
    """

    with open(path, 'r') as file:
        text = file.read()
        if MOSKOW in text:
            return MOSKOW
        elif PITER in text:
            return PITER
        else:
            return None


def gen_six_digit_tickets():
    """
    The function returns a list of six-digit numbers in a range from 000001 to 999999
    """
    all_tickets = [''.join(i) for i in itertools.product("0123456789", repeat=6)]
    return all_tickets


class LuckyTickets:
    def __init__(self, list_of_tickets):
        self.list_of_tickets = list_of_tickets

    def get_moscow(self):
        """
        The method counts the tickets which numbers match the rule:
        the sum of the first tree digits is equal to the sum of the last tree digits
        """
        num_moscow_lucky_tickets = 0
        for i in self.list_of_tickets:
            if sum(map(int, str(int(i) // 1000))) == sum(map(int, str(int(i) % 1000))):
                num_moscow_lucky_tickets += 1
        return num_moscow_lucky_tickets

    def get_peter(self):
        """
        The method counts the tickets which numbers match the rule:
        the sum of the even digits is equal to the sum of the odd digits
        """
        num_piter_lucky_tickets = 0
        for i in self.list_of_tickets:
            if sum(int(n) for n in i if int(n) % 2 == 0) == \
                    sum(int(n) for n in i if int(n) % 2 != 0):
                num_piter_lucky_tickets += 1
        return num_piter_lucky_tickets


def main():
    """
    The function gets the path to the file and reads it to get the word
    to choose the algorithm to count the tickets. Then, a list of six-digit
    numbers is generated and an instance of Tickets class is created. Next,
    the the tickets are counted, accordingly to the chosen algorithm
    """
    try:
        path = get_path()
        choice = read_file(path)
        list_of_all_tickets = gen_six_digit_tickets()
        t = LuckyTickets(list_of_all_tickets)
        if choice == MOSKOW:
            print(t.get_moscow())
        elif choice == PITER:
            print(t.get_peter())
    except FileNotFoundError:
        print(FILE_NOT_FOUND_MSG)


if __name__ == '__main__':
    main()
