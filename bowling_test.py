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
        self.assertEqual(calc_score("X X 23 33"), 48)

    def test_does_ten_frames(self):
        self.assertEqual(calc_score("11 X 11 1/ 11 11 11 11 11 11"), 39)
    
    def test_does_bonus_rolls(self):
        self.assertEqual(calc_score("11 X 11 1/ 11 11 11 11 11 X 11"), 51)
    
    def test_does_bonus_rolls_with_spare(self):
        self.assertEqual(calc_score("11 X 11 1/ 11 11 11 11 11 X 1/"), 57)
        
class TestEdgeCases(unittest.TestCase):
    def test_does_end_strike(self):
        self.assertEqual(calc_score("11 11 11 X"), 16)
    
    def test_does_end_spare(self):
        self.assertEqual(calc_score("11 11 11 4/"), 16)