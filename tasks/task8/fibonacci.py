import argparse


INCORRECT_NUM_MSG = 'The list could not been generated. Positive integers should be entered'


def get_numbers():
    """
    The function defines which arguments are required and parses them from a command-line.
    The help and usage messages are generated in case of entering incorrect data
    """

    parser = argparse.ArgumentParser(description='Get integers')
    parser.add_argument('integer1', type=int, help='A positive integer')
    parser.add_argument('integer2', type=int, help='A positive integer')
    args = parser.parse_args()
    num1 = args.integer1
    num2 = args.integer2
    return num1, num2


class FibonacciSequence:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def fibonacci(self):

        # yields a positive integer
        a, b = 0, 1
        while a < self.num2:
            yield a
            a, b = b, a + b

    @staticmethod
    def get_index(fib_list, n):

        # returns an index of a given number in a given list
        i = fib_list.index(n)
        return i

    def get_fib_sequence(self):
        """
        the method generates a sequence of fibonacci numbers in a range from 0 to
        a number 'number2' which is parsed from a command-line
        """

        fibonacci_sequence = [n for n in self.fibonacci()]
        return fibonacci_sequence

    def fib_list(self):
        """
        the method takes a sequence of fibonacci numbers and returns
        a list of fibonacci numbers in a range from 'number1 to 'number2
        which are parsed from a command-line
        """
        fibonacci_list = self.get_fib_sequence()
        if self.num1 in fibonacci_list:
            i = self.get_index(fibonacci_list, self.num1)
            res = fibonacci_list[i:]
        else:
            nearest_num = min(fibonacci_list, key=lambda x: abs(x-self.num1))
            i = self.get_index(fibonacci_list, nearest_num)
            res = fibonacci_list[i+1:]
        return res

    def __repr__(self):
        if self.num1 > self.num2:
            print(f'The fibonacci sequence in range from {self.num1} to {self.num2} is empty : ')
        else:
            print(f'The fibonacci sequence in range from {self.num1} to {self.num2} is: ')


def main():
    numbers = get_numbers()
    num1 = numbers[0]
    num2 = numbers[1]
    try:
        f = FibonacciSequence(num1, num2)
        f.__repr__()
        print(*f.fib_list(), sep=', ')
    except ValueError:
        print(INCORRECT_NUM_MSG)


if __name__ == '__main__':
    main()
