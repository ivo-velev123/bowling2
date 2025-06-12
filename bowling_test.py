import unittest
from bowling import *

class TestCalcScore(unittest.TestCase):
    def test_does_simple_rolls(self):
        self.assertEqual(calc_score("11 11 11 11"), 8)

    def test_does_strike(self):
        self.assertEqual(calc_score("X 11 54 81"), 32)
    
    def test_does_spare(self):
        self.assertEqual(calc_score("4/ 11 11 11"), 17)
    
    def test_does_double_strike(self):
        self.assertEqual(calc_score("X X 23 33"), 51)

class TestEdgeCases(unittest.TestCase):
    def test_does_end_X(self):
        self.assertEqual(calc_score("11 11 11 X"), 16)