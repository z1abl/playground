import unittest
from .solution import Solution

class TestValidParentheses(unittest.TestCase):
    def test_valid_parentheses(self):
        solution = Solution()
        test_valid_parentheses = solution.isValid
        self.assertEqual(test_valid_parentheses('()()()'), True)
        self.assertEqual(test_valid_parentheses('[(()()())'), False)
        self.assertEqual(test_valid_parentheses('][)'), False)
        self.assertEqual(test_valid_parentheses('{{]{}]][}}'), False)
        self.assertEqual(test_valid_parentheses('[][][][]'), True)
        self.assertEqual(test_valid_parentheses('[{(()}]'), False)
        self.assertEqual(test_valid_parentheses('[{}}}}]'), False)
        self.assertEqual(test_valid_parentheses('[((())]'), False)

