import unittest
from utilities import average

class TestAverage(unittest.TestCase):

    def test_average_list(self):
        self.assertEqual(average([10.0, 5.0, 15.0]), 10.0, "Should be 10.0")

    def test_average_tuple(self):
        self.assertEqual(average((1.0, 2.0, 3.0)), 2.0, "Should be 2.0")

if __name__ == '__main__':
    unittest.main()