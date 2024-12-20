# Todo Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num
        return 1 + (num - 1) % 9

# Time and space complexity are O(1)