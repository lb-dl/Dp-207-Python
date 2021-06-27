import argparse

INCORRECT_VALUE_MSG = 'The entered value is incorrect. ' \
                      'Enter a positive integer less than 1.000.000.000'
ZERO = ('ноль',)

ONES_FEMININE = {
    1: ('одна',),
    2: ('две',),
    3: ('три',),
    4: ('четыре',),
    5: ('пять',),
    6: ('шесть',),
    7: ('семь',),
    8: ('восемь',),
    9: ('девять',),
}

ONES = {
    1: ('один',),
    2: ('два',),
    3: ('три',),
    4: ('четыре',),
    5: ('пять',),
    6: ('шесть',),
    7: ('семь',),
    8: ('восемь',),
    9: ('девять',),
}

TENS = {
    0: ('десять',),
    1: ('одиннадцать',),
    2: ('двенадцать',),
    3: ('тринадцать',),
    4: ('четырнадцать',),
    5: ('пятнадцать',),
    6: ('шестнадцать',),
    7: ('семнадцать',),
    8: ('восемнадцать',),
    9: ('девятнадцать',),
}

TWENTIES = {
    2: ('двадцать',),
    3: ('тридцать',),
    4: ('сорок',),
    5: ('пятьдесят',),
    6: ('шестьдесят',),
    7: ('семьдесят',),
    8: ('восемьдесят',),
    9: ('девяносто',),
}

HUNDREDS = {
    1: ('сто',),
    2: ('двести',),
    3: ('триста',),
    4: ('четыреста',),
    5: ('пятьсот',),
    6: ('шестьсот',),
    7: ('семьсот',),
    8: ('восемьсот',),
    9: ('девятьсот',),
}

ABOVE_HUNDREDS = {
    1: ('тысяча', 'тысячи', 'тысяч',),
    2: ('миллион', 'миллиона', 'миллионов',),
}


class NumberToWords(object):
    def __init__(self, number_to_words=0):
        self.number = int(number_to_words)

    def print_word(self):
        print(self.number_to_words(self.number))

    @staticmethod
    def add_prefix_above_hundreds(remainder, forms):
        if remainder % 100 < 10 or remainder % 100 > 20:
            if remainder % 10 == 1:
                form = 0
            elif 1 < remainder % 10 < 5:
                form = 1
            else:
                form = 2
        else:
            form = 2
        return forms[form]

    @staticmethod
    def three_digit_groups(number, separating_length):

        """
        The method splits a given number into tree-digit groups, e.g. 100890 => [100, 890]
        """
        all_length = len(number)
        if all_length > separating_length:
            start = all_length % separating_length
            if start > 0:
                result = number[:start]
                yield int(result)
            for i in range(start, all_length, separating_length):
                result = number[i:i + separating_length]
                yield int(result)
        else:
            yield int(number)

    @staticmethod
    def get_digits(number):
        """
        The method splits a three-digit number into digits, e.g. 100 => [0, 0, 1]
        """
        array_of_digits = [int(digit) for digit in reversed(list(('%03d' % number)[-3:]))]
        return array_of_digits

    def number_to_words(self, entered_number, feminine=False):
        """
        The method calls for 'three_digit_groups' and 'get_digits' methods. Then it turns
        a single digit into its word representation. The method adds the words like
        'тысяча' or 'миллион', if necessary, calling 'add_prefix_above_hundreds' method,
        e.g. 100890 => 'сто тысяч восемьсот девяносто'
        """
        if int(entered_number) == 0:
            return ZERO[0]
        else:
            words_to_print = []
            parts = list(self.three_digit_groups(str(entered_number), 3))
            i = len(parts)
            for part in parts:
                i -= 1
                n1, n2, n3 = self.get_digits(part)
                if n3 > 0:
                    words_to_print.append(HUNDREDS[n3][0])
                if n2 > 1:
                    words_to_print.append(TWENTIES[n2][0])
                if n2 == 1:
                    words_to_print.append(TENS[n1][0])
                elif n1 > 0:
                    if i == 1 or feminine and i == 0:
                        ones = ONES_FEMININE
                    else:
                        ones = ONES
                    words_to_print.append(ones[n1][0])
                if i > 0 and part != 0:
                    words_to_print.append(self.add_prefix_above_hundreds(part, ABOVE_HUNDREDS[i]))

            return ' '.join(words_to_print)


def get_number():
    """
        The function defines which argument is required and parses it from a command-line.
        The help and usage messages are generated in case of entering incorrect data
        """
    parser = argparse.ArgumentParser(description='Get an integer')
    parser.add_argument('integer', type=int, help='A positive integer')
    args = parser.parse_args()
    num = args.integer
    return num


def main():
    """
        The function gets the number to be converted into words.
        Then, an instance of NumberToWords class is created and
        the number's word representation is printed.
        """
    number_to_convert = get_number()
    try:
        n = NumberToWords(number_to_convert)
        print(n.number_to_words(number_to_convert))
    except (KeyError, ValueError):
        print(INCORRECT_VALUE_MSG)


if __name__ == '__main__':
    main()
