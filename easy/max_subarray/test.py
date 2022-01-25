import unittest
from .solution import Solution

class TestMaxSubarray(unittest.TestCase):
    def test_max_subarray(self):
        solution = Solution()
        maxSubArray = solution.maxSubArray
        self.assertEqual(maxSubArray([1]), 1)
        self.assertEqual(maxSubArray([-1]), -1)
        self.assertEqual(maxSubArray([-1,1]), 1)
        self.assertEqual(maxSubArray([1,2,3,4,5]), 15)
        self.assertEqual(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(maxSubArray([-5,-1,-100,100,50,1,-4,-8]), 151)
        self.assertEqual(maxSubArray([-1,-2,17,-1,30]), 46)


