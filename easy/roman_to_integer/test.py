import unittest
from .solution import Solution

class TestRomanToInteger(unittest.TestCase):
    def test_convert_roman_to_integer(self):
        solution = Solution()
        romanToInt = solution.romanToInt
        self.assertEqual(romanToInt('X'), 10)
        self.assertEqual(romanToInt('V'), 5)
        self.assertEqual(romanToInt('III'), 3)
        self.assertEqual(romanToInt('IX'), 9)
        self.assertEqual(romanToInt('IV'), 4)
        self.assertEqual(romanToInt('MCMXCIV'), 1994)
        self.assertEqual(romanToInt('LVIII'), 58)
        self.assertEqual(romanToInt('MDCXCV'), 1695)

        romanToIntElegant = solution.romanToIntElegant
        self.assertEqual(romanToIntElegant('X'), 10)
        self.assertEqual(romanToIntElegant('V'), 5)
        self.assertEqual(romanToIntElegant('III'), 3)
        self.assertEqual(romanToIntElegant('IX'), 9)
        self.assertEqual(romanToIntElegant('IV'), 4)
        self.assertEqual(romanToIntElegant('MCMXCIV'), 1994)
        self.assertEqual(romanToIntElegant('LVIII'), 58)
        self.assertEqual(romanToIntElegant('MDCXCV'), 1695)

if __name__ == '__main__':
    unittest.main()