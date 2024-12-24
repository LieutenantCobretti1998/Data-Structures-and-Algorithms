# Todo Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#  Note that you must do this in-place without making a copy of the array.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pos = 0

        for num in nums:
            if num != 0:
                nums[non_zero_pos] = num
                non_zero_pos += 1

        for i in range(non_zero_pos, len(nums)):
            nums[i] = 0

# The time and space complexity is O(n) and O(1) respectively