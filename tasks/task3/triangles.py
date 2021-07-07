from math import sqrt

INSTRUCTIONS = 'Enter a name and three sides of a triangle, separated by commas "," (e.g "triangle, 4, 5, 6") \n'
OUTPUT_STR = '============= Triangles list: ==============='
NOT_EXISTED_TRIANGLE = 'There is not a triangle with entered sides'
MESSAGE = 'Would you like to continue? Enter "yes" or "y" to continue. Press another button to quit \n'
INVALID_DATA_MSG = 'Entered data is incorrect. Try again, please'


def main():
    """
    While a programme runs, the function creates a triangle, calling the method
    'create_triangle' and appends it into a list, in case the triangle is not 'None'.
    When the programme stops, the method 'sort_triangles' is called and a sorted
    list of triangles is printed line by line.
    """
    list_of_triangles = []
    run = True
    while run:
        a_triangle = create_triangle()
        if a_triangle:
            list_of_triangles.append(a_triangle)
        run = is_exit()

    print(OUTPUT_STR)
    list_of_sorted_triangles = sort_triangles(list_of_triangles)
    for triangle in list_of_sorted_triangles:
        triangle.__repr__()


def create_triangle():
    """
    The function asks for the user input. If the input data is valid,
    an instance 'triangle' is created and returned. Else, the message about invalid data is printed.
    """
    user_input = get_user_input()
    if user_input:
        try:
            values = user_input.split(',')
            if len(values) != 4:
                print(INVALID_DATA_MSG)
            else:
                triangle_name = values[0]
                side_a = float(values[1])
                side_b = float(values[2])
                side_c = float(values[3])
                if validation(side_a) and validation(side_b) and validation(side_c):
                    triangle = Triangle(triangle_name, side_a, side_b, side_c)
                    if triangle.is_triangle():
                        return triangle
                    else:
                        print(NOT_EXISTED_TRIANGLE)
                else:
                    print(INVALID_DATA_MSG)
                    pass
        except ValueError:
            print(INVALID_DATA_MSG)


def sort_triangles(list_):
    # sort triangles by their area
    sorted_triangles = sorted(list_, key=lambda x: x.get_area(), reverse=True)
    return sorted_triangles


def get_user_input():

    # Ask users for input
    user_input = input(INSTRUCTIONS)
    return user_input


def validation(value):
    """
    The function checks and returns 'True' if the entered values are numbers greater than 0
    and the numbers' type is float. Otherwise, it returns 'False'.
    """
    return isinstance(value, float) and value > 0


def is_exit():
    """
    The function checks for the user input in order to continue (returns 'True')
    or quit a programme (returns 'False')
    """
    answer = input(MESSAGE)
    return answer.lower() in ['y', 'yes']


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

        # Counts and returns a square of a triangle using Heron formula
        p = 0.5*(self.side_a + self.side_b + self.side_c)
        self.area = round(sqrt(p*(p - self.side_a) * (p - self.side_b) * (p - self.side_c)), 2)
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
