import unittest
from lab2 import board_space

class TestCheckResult(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(board_space(10, 2, 3), 9)

    def test_example_2(self):
        self.assertEqual(board_space(2, 1000000000, 999999999), 1999999998)

    def test_example_3(self):
        self.assertEqual(board_space(4, 1, 1), 2)

if __name__ == '__main__':
    unittest.main()