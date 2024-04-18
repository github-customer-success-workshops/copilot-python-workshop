import unittest
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(3, 2), 1)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(Calculator.divide(6, 2), 3)

if __name__ == '__main__':
    unittest.main()