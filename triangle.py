def area(a, b, c):
    '''
    Takes numbers a, b, c - the sides of a triangle.
    Returns the semi-sum of the sides of the triangle (semi-perimeter).

    Example call:
    semi_perimeter = area(3, 4, 5)
    print(semi_perimeter)
    6.0
    '''
    return (a + b + c) / 2


def perimeter(a, b, c):
    '''
    Takes numbers a, b, c - the sides of a triangle.
    Returns the sum of the sides of the triangle (perimeter).

    Example call:
    triangle_perimeter = perimeter(3, 4, 5)
    print(triangle_perimeter)
    12
    '''
    return a + b + c