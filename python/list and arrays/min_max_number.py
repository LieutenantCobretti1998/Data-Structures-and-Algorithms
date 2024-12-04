# TODO You are given a 0-indexed integer array nums whose length is a power of 2.
#  Apply the following algorithm on nums:
#  Let n be the length of nums. If n == 1, end the process.
#  Otherwise, create a new 0-indexed integer array newNums of length n / 2.


def minMaxGame(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        while len(nums) > 1:
            new_nums = []
            n = len(nums)
            for i in range(n // 2):
                if i % 2 == 0:
                    new_nums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    new_nums.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = new_nums
        return nums[0]


print(minMaxGame([1, 2, 3, 4]))

"""
    Time and Space Complexity: O(n)
"""