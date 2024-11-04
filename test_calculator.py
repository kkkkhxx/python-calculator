import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)
    
    def test__add_zero_negative(self):
        self.assertEqual(self.calc.add(-3, 0), -3)

    #test methods subtract:
    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(-1, -5), 4)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(-1, 3), -4)

    #test methods multiply:
    def test_mul(self):
        self.assertEqual(self.calc.multiply(4, 8), 32)

    def test_mul_zero(self):
        self.assertEqual(self.calc.multiply(0, 8), 0)

    def test_mul_negative(self):
        self.assertEqual(self.calc.multiply(-2, -8), 16)

    def test_mul_negative_num(self):
        self.assertEqual(self.calc.multiply(2, -8), -16)
    
    #test methods divide:
    def test_div_num(self):
        self.assertEqual(self.calc.divide(9, 3), 3)

    def test_div_negative(self):
        self.assertEqual(self.calc.divide(0, 9), 0)

    #test methods modulo:
    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)
    
    def test_modulo_num(self):
        self.assertEqual(self.calc.modulo(3, 7), 3)
    

if __name__ == '__main__':
    unittest.main()