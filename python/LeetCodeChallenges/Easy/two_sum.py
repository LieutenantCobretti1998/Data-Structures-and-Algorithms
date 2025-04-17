# TODO Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# TODO You may assume that each input would have exactly one solution, and you may not use the same element twice.
# TODO You can return the answer in any order.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i



