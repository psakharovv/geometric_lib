import unittest
from calculate import calc


class TestCalculate(unittest.TestCase):

    def test_calc_circle_area(self):
        fig = 'circle'
        func = 'area'
        size = [3]
        expected_result = 28.274333882308138
        result = calc(fig, func, size)
        self.assertAlmostEqual(result, expected_result)

    def test_calc_circle_perimeter(self):
        fig = 'circle'
        func = 'perimeter'
        size = [3]
        expected_result = 18.84955592153876
        result = calc(fig, func, size)
        self.assertAlmostEqual(result, expected_result)

    def test_calc_square_area(self):
        fig = 'square'
        func = 'area'
        size = [4]
        expected_result = 16
        result = calc(fig, func, size)
        self.assertAlmostEqual(result, expected_result)

    def test_calc_square_perimeter(self):
        fig = 'square'
        func = 'perimeter'
        size = [4]
        expected_result = 16
        result = calc(fig, func, size)
        self.assertAlmostEqual(result, expected_result)

    def test_calc_incorrect_figure(self):
        fig = 'triangle'
        func = 'area'
        size = [3, 4, 5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_incorrect_function(self):
        fig = 'circle'
        func = 'volume'
        size = [3]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_calc_incorrect_size(self):
        fig = 'circle'
        func = 'area'
        size = [3, 4]
        with self.assertRaises(TypeError):
            calc(fig, func, size)


if __name__ == '__main__':
    unittest.main()
