import unittest
import math
import sys

sys.path.append("..")

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_negative_radius_area(self):
        radius = -1
        with self.assertRaises(ValueError):
            area(radius)

    def test_negative_radius_perimeter(self):
        radius = -1
        with self.assertRaises(ValueError):
            perimeter(radius)

    def test_zero_radius_area(self):
        radius = 0
        expected_area = 0
        self.assertEqual(area(radius), expected_area)

    def test_zero_radius_perimeter(self):
        radius = 0
        expected_perimeter = 0
        self.assertEqual(perimeter(radius), expected_perimeter)

    def test_positive_radius_area(self):
        radius = 1
        expected_area = math.pi
        self.assertEqual(area(radius), expected_area)

    def test_positive_radius_perimeter(self):
        radius = 1
        expected_perimeter = 2 * math.pi
        self.assertEqual(perimeter(radius), expected_perimeter)


if __name__ == "__main__":
    unittest.main()
