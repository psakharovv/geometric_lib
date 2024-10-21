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