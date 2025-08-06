'''import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.Testcase):
    def SetUp(self):
        self.calc=SimpleCalculator()
'''

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
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,4),1)
        self.assertEqual(self.calc.subtract(4,8),-4)

    def test_multiply(self):
         self.assertEqual(self.calc.multiply(5,4),20)
         self.assertEqual(self.calc.multiply(3,3),9)
        
    def test_divide(self):
        try:
            self.assertEqual(self.calc.divide(9,3),3)
            self.assertEqual(self.calc.divide(8,4),2)

        except ZeroDivisionError:
            return f"Cannot divide by zero"
            
# Remember to write additional test methods for subtract, multiply, and divide.
