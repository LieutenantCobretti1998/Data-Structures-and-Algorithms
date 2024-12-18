#Todo Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > len(nums) // 2:
                return num


# Time and Space complexity is O(n)

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

# This is Boyer-Moore algorithm which works because The majority element has more "votes"
# than all other elements combined. and even the count drops to 0, the majority element will dominate when it resets.
# Time and Space complexity is O(n) and O(1), respectively