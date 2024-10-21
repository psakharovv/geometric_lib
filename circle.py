import math

def area(r):
    '''
    Takes a number r - the radius of a circle,
    and returns the area of the circle calculated as pi multiplied by the square of the radius.

    Example call:
    circle_area = area(5)
    print(circle_area)
    78.53981633974483
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Takes a number r - the radius of a circle,
    and returns the circumference of the circle calculated as 2 multiplied by pi and the radius.

    Example call:
    circle_perimeter = perimeter(5)
    print(circle_perimeter)
    31.41592653589793
    '''
    return 2 * math.pi * r