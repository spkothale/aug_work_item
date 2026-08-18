import unittest
from src.BodmasCalc import Bodmas


class TestBodmas(unittest.TestCase):

    def test_addition(self):
        calculator = Bodmas()
        result = calculator.calculate("2+3*4")
        self.assertEqual(result, 14)

    def test_subtraction(self):
        calculator = Bodmas()
        result = calculator.calculate("3*4-5*2")
        self.assertEqual(result, 2)

    def test_division(self):
        calculator = Bodmas()
        result = calculator.calculate("2+8/4")
        self.assertEqual(result, 4)

    def test_addition(self):
        calculator = Bodmas()
        result = calculator.calculate("3*4+2*2")
        self.assertEqual(result, 16)


if __name__ == "__main__":
    unittest.main()