from math import sqrt

INSTRUCTIONS = 'Enter a name and three sides of a triangle, separated by commas "," (e.g "name, 4, 5, 6")'
HELP_MSG = 'The triangle sides must be numbers greater than 0. Try again, please'
OUTPUT_STR = '============= Triangles list: ==============='
NOT_EXISTED_TRIANGLE = 'There is not a triangle with entered sides'


def main():
    list_of_triangles = []
    run = True
    while run:
        try:
            print(INSTRUCTIONS)
            user_input = input()
            if user_input:
                values = user_input.split(',')
                triangle_name = values[0]
                side_a = float(values[1])
                side_b = float(values[2])
                side_c = float(values[3])
                if validation(side_a) and validation(side_b) and validation(side_c):
                    triangle = Triangle(triangle_name, side_a, side_b, side_c)
                    if triangle.is_triangle():
                        list_of_triangles.append(triangle)
                    else:
                        print(NOT_EXISTED_TRIANGLE)
                else:
                    print(HELP_MSG)
        except ValueError:
            print(HELP_MSG)
        run = is_exit()

    # sort triangles by their square
    sorted_triangles = sorted(list_of_triangles, key=lambda x: x.get_area(), reverse=True)
    print(OUTPUT_STR)
    for triangle in sorted_triangles:
        triangle.__repr__()


def validation(value):
    """
    The function checks and returns 'True' if the entered values are numbers greater than 0.
    Otherwise, it prints a message with the further instructions and returns 'False'.
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
    answer = input(f'Would you like to continue? Enter "yes" or "y" to continue. '
                   f'Press any other button to quit')
    if answer.lower() in ['y', 'yes']:
        return True
    else:
        return False


class Triangle:
    """
    Class Triangle
    """

    def __init__(self, name, side_a, side_b, side_c):
        self.name = name
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.area = 0

    def get_area(self):

        # Counts and returns a square of a triangle
        p = 0.5*(self.side_a + self.side_b + self.side_c)
        self.area = sqrt(p*(p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        return self.area

    def is_triangle(self):

        # Checks if a triangle with the given sides exists
        if self.side_a + self.side_b > self.side_c and \
            self.side_a + self.side_c > self.side_b and \
                self.side_c + self.side_b > self.side_a:
            return True
        else:
            return False

    def __repr__(self):
        print('[' + self.name + ']: ' + str(self.area) + ' cm')


if __name__ == '__main__':
    main()
