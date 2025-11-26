import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_normal(self):
        self.assertEqual(area(5, 4), 20)

    def test_perimeter(self):
        self.assertEqual(perimeter(5, 4), 18)

if __name__ == '__main__':
    unittest.main()
