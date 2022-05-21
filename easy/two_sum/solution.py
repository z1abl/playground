# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
from typing import List

class Solution:
    def twoSumBruto(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            el = nums[i]
            diff = target - el
            for j in range(i+1,len(nums)):
                if nums[j] == diff:
                    print(i,j)
                    return [i,j]


    def twoSumMap(self, nums: List[int], target: int) -> List[int]:
        arch_nums = {}
        for i in range(0,len(nums)):
            diff = target - nums[i]
            # if diff in arch_nums.__contains__(diff)
            if diff in arch_nums.keys():
                print(i, arch_nums[diff])
                return [i,arch_nums[diff]]
            else:
                arch_nums[nums[i]] = i