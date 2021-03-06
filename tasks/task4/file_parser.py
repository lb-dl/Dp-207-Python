INSTRUCTIONS = 'There are two modes in the programme: \n' \
               '1. Count a number of the string in the file \n' \
               '2. Find and replace the string in the file \n' \
               'To choose the mode enter the data: \n' \
               'For mode 1:path to the file and string to count: e.g. file.txt, string to find \n' \
               'For mode 2:path to the file, old string, new string: e.g. file.txt, old string, new string \n'
STRING_NOT_FOUND_MSG = "There aren't any occurrences of a given string in the file"
FILE_NOT_FOUND_MSG = 'File not found'
INCORRECT_PARAMS = 'Entered data is not correct'
MESSAGE = 'Would you like to continue? Enter "yes" or "y" to continue. Enter another button to stop \n'


class FileParser:
    def __init__(self, path):
        self.path = path


class CountString(FileParser):
    def __init__(self, path, string_to_count):
        super().__init__(path)
        self.string_to_count = string_to_count
        self.result = 0

    def get_number_of_given_str(self):
        """
        The method reads a file and returns a number of occurrences of a given string in the file
        """
        self.result = 0
        with open(self.path, 'r') as file:
            self.result = file.read().count(self.string_to_count)
        return f'{self.result} strings were found in the file\n'


class ReplaceString(FileParser):
    def __init__(self, path, string_to_replace, new_string):
        super().__init__(path)
        self.string_to_replace = string_to_replace
        self.new_string = new_string

    def replace_str(self):
        """
        The method reads a file. If a given string is found,
        this string is replaced with the new string.
        """
        with open(self.path, 'r') as file:
            text = file.read()
            if self.string_to_replace in text:
                res = text.replace(self.string_to_replace, self.new_string)
                with open(self.path, 'w') as f:
                    f.write(res)
                print(f'The string "{self.string_to_replace}" was successfully replaced by "{self.new_string}"\n')
            else:
                print(STRING_NOT_FOUND_MSG)


def get_params():
    """
    The function asks for the user input. Then, it splits the input string.
    In case there are 2 or 3 parameters, the function returns them.
    """
    user_choice = input(INSTRUCTIONS)
    user_choice = user_choice.replace("'", "")
    list_of_params = [x.strip() for x in user_choice.split(',')]
    if len(list_of_params) < 2 or len(list_of_params) > 3:
        pass
    else:
        return list_of_params


def is_exit():
    """
    The function checks for the user input in order to continue (returns 'True')
    or quit a programme (returns 'False')
    """
    answer = input(MESSAGE)
    return answer.lower() in ['y', 'yes']


def main():
    """
    The function checks the number of parameters to start the certain mode of a program.
    If there are 2 parameters, the function creates an instance of "CountString" class
    and calls for "get_number_of_given_str()" method. If there are 3 parameters, an instance
    of "ReplaceString" class is created and the method "replace_str()" is called.
    """
    run = True
    while run:
        params = get_params()
        try:
            if len(params) == 2:
                count_str = CountString(params[0], params[1])
                res = count_str.get_number_of_given_str()
                print(res)
            elif len(params) == 3:
                replace_str = ReplaceString(params[0], params[1], params[2])
                replace_str.replace_str()
        except FileNotFoundError:
            print(FILE_NOT_FOUND_MSG)
        except TypeError:
            print(INCORRECT_PARAMS)
        run = is_exit()


if __name__ == '__main__':
    main()
