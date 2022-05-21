import unittest
from .solution import Solution

class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()
        test_two_sum_bruto = solution.twoSumBruto
        test_two_sum_map = solution.twoSumMap

        self.assertEqual(test_two_sum_bruto([2,7,11,15],9),[0,1])
        self.assertEqual(test_two_sum_bruto([3,2,4],6),[1,2])
        self.assertEqual(test_two_sum_bruto([3,3],6),[0,1])

        self.assertEqual(test_two_sum_map([2,7,11,15],9),[1,0])
        self.assertEqual(test_two_sum_map([3,2,4],6),[2,1])
        self.assertEqual(test_two_sum_map([2,3,1,4],6),[3,0])


