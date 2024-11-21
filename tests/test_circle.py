import unittest
from circle import area, perimeter


class TestCircle(unittest.TestCase):

    def test_area(self):
        r = 1
        expected_result = 3.141592653589793
        result = area(r)
        self.assertAlmostEqual(result, expected_result, places=7)

        r = 2
        expected_result = 12.566370614359172
        result = area(r)
        self.assertAlmostEqual(result, expected_result, places=7)

        r = 3
        expected_result = 28.274333882308138
        result = area(r)
        self.assertAlmostEqual(result, expected_result, places=7)

    def test_perimeter(self):
        r = 1
        expected_result = 6.283185307179586
        result = perimeter(r)
        self.assertAlmostEqual(result, expected_result, places=7)

        r = 2
        expected_result = 12.566370614359172
        result = perimeter(r)
        self.assertAlmostEqual(result, expected_result, places=7)

        r = 3
        expected_result = 18.84955592153876
        result = perimeter(r)
        self.assertAlmostEqual(result, expected_result, places=7)


if __name__ == '__main__':
    unittest.main()
