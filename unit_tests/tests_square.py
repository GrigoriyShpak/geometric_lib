import unittest
import sys

sys.path.append("..")

from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_negative_side(self):
        side = -1
        with self.assertRaises(ValueError):
            area(side)

    def test_negative_side(self):
        side = -1
        with self.assertRaises(ValueError):
            perimeter(side)

    def test_zero_side(self):
        side = 0
        excepted_area = 0
        excepted_perimeter = 0
        self.assertEqual(area(side), excepted_area)

    def test_zero_side(self):
        side = 0
        excepted_area = 0
        excepted_perimeter = 0
        self.assertEqual(perimeter(side), excepted_perimeter)

    def test_positive_side(self):
        side = 1
        excepted_area = 1
        excepted_perimeter = 4
        self.assertEqual(area(side), excepted_area)

    def test_positive_side(self):
        side = 1
        excepted_area = 1
        excepted_perimeter = 4
        self.assertEqual(perimeter(side), excepted_perimeter)
