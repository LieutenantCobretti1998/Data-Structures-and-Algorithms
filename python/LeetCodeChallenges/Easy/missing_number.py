# Todo Given an array nums containing n distinct numbers in the range [0, n],
#  return the only number in the range that is missing from the array.
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Time and Space complexity are O(n) due to sum function and O(1), respectively

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

# Time and Space complexity are O(nlog n) due to sort function and O(1), respectively