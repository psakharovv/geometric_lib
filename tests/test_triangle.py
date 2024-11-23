import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):

    def test_area(self):
        a, b, c = 3, 4, 5
        expected_result = 6.0
        result = area(a, b, c)
        self.assertAlmostEqual(result, expected_result)

        a, b, c = 6, 8, 10
        expected_result = 24.0
        result = area(a, b, c)
        self.assertAlmostEqual(result, expected_result)

        a, b, c = 7, 24, 25
        expected_result = 84.0
        result = area(a, b, c)
        self.assertAlmostEqual(result, expected_result)

    def test_perimeter(self):
        a, b, c = 3, 4, 5
        expected_result = 12
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_result)

        a, b, c = 6, 8, 10
        expected_result = 24
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_result)

        a, b, c = 7, 24, 25
        expected_result = 56
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
