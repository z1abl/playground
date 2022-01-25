import math
from typing import List

class Solution:
    # Kadane's Algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        final_sum = -math.inf

        for num in nums:
            curr_sum += num
            if curr_sum > final_sum:
                final_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        print(final_sum)
        return final_sum

