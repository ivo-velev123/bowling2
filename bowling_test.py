import unittest
from bowling import calc_score

class TestCalcScore(unittest.TestCase):
    def test_does_simple_numbers(self):
        self.assertEqual(calc_score("11 11 11 11"), 8)

    def test_does_X(self):
        self.assertEqual(calc_score("X 11 54 81"), 30)
    
    def test_does_slash(self):
        self.assertEqual(calc_score("4/ 11 11 X"), 24)