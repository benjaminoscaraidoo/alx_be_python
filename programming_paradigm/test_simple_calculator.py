import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3), 2)
        self.assertEqual(self.calc.subtract(1,9), -8)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,4), 8)
        self.assertEqual(self.calc.multiply(3,0), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(6,2), 3)
        self.assertEqual(self.calc.divide(3,0), "Error: Cannot divide by zero." )
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.