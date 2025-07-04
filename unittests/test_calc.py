import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)

sys.path.append(parent)

from calc import Calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(2, 0), 2)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 3), -1)
        self.assertEqual(self.calc.sub(2, 0), 2)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 6), 12)
        self.assertEqual(self.calc.mul(2, 0), 0)

    def test_div(self):
        self.assertEqual(self.calc.div(6, 2), 3)
        # with self.assertRaises(ZeroDivisionError):
        #     self.calc.div(5, 0)
        self.assertRaises(ZeroDivisionError, self.calc.div, 5, 0)

    def test_pow(self):
        self.assertEqual(self.calc.pow(2, 3), 8)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(4), 2)
        self.assertAlmostEqual(self.calc.sqrt(2), 1.41421356237, places=7)
