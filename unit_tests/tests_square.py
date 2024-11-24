import unittest
import sys
from square import area, perimeter

sys.path.append("..")


class SquareTestCase(unittest.TestCase):

    def test_negative_side_area(self):
        side = -1
        with self.assertRaises(ValueError):
            area(side)

    def test_negative_side_perimeter(self):
        side = -1
        with self.assertRaises(ValueError):
            perimeter(side)

    def test_zero_side_area(self):
        side = 0
        excepted_area = 0
        self.assertEqual(area(side), excepted_area)

    def test_zero_side_perimeter(self):
        side = 0
        excepted_perimeter = 0
        self.assertEqual(perimeter(side), excepted_perimeter)

    def test_positive_side_area(self):
        side = 1
        excepted_area = 1
        self.assertEqual(area(side), excepted_area)

    def test_positive_side_perimeter(self):
        side = 1
        excepted_perimeter = 4
        self.assertEqual(perimeter(side), excepted_perimeter)
