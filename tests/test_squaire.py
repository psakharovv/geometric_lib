import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area(self):
        a = 1
        expected_result = 1
        result = area(a)
        self.assertEqual(result, expected_result)

        a = 2
        expected_result = 4
        result = area(a)
        self.assertEqual(result, expected_result)

        a = 3
        expected_result = 9
        result = area(a)
        self.assertEqual(result, expected_result)

    def test_perimeter(self):
        a = 1
        expected_result = 4
        result = perimeter(a)
        self.assertEqual(result, expected_result)

        a = 2
        expected_result = 8
        result = perimeter(a)
        self.assertEqual(result, expected_result)

        a = 3
        expected_result = 12
        result = perimeter(a)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
