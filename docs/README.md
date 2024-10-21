
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# General Description of the Solution
This calculator is designed to compute the area and perimeter of various geometric shapes: circles and squares. The user inputs the name of the shape, the required function (area or perimeter), and the dimensions of the shape. The calculator uses mathematical formulas to calculate the result and displays it on the screen

# Description of each function with examples of calls
## Triangle
```python
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
```

## Square
```python
def area(a):
    ''' 
    Takes a number a - the side of a square, 
    and returns the square of the number a - the area of the square with side a.

    Example call:
    square_area = area(5)
    print(square_area)
    25
    '''
    return a * a


def perimeter(a):
    ''' 
    Takes a number a, where a is the side of a square, 
    and returns the number a multiplied by 4 - the perimeter of the square with side a.

    Example call:
    square_perimeter = perimeter(5)
    print(square_perimeter)
    20
    '''
    return 4 * a
```

## Circle
```python
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
```

## Calculate
```python
import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):
    """Calculates the specified function (perimeter or area) for the given figure
    with the provided dimensions.

    Parameters:
    fig: Name of the figure (e.g., 'circle' or 'square').
    func: Name of the function (e.g., 'perimeter' or 'area').
    size: A list of dimensions needed to compute the function.

    Example call:
    calc('circle', 'area', [5])
    # Output: area of circle is 78.53981633974483
    """
    assert fig in figs
    assert func in funcs

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')


if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and squaren").split(' ')))

    calc(fig, func, size)
```

# Project Change History
- b5b0fae (origin/develop, develop) L-04: Update docs for calculate.py
- d76db2a L-04: Add calculate.py
- 51c40eb L-04: Doc updated for triangle
- d080c78 L-04: Triangle added
- d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
- 8ba9aeb L-03: Circle and square added