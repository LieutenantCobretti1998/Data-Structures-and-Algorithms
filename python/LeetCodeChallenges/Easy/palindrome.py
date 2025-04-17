# TODO Given an integer x, return true if x is a palindrome, and false otherwise.

# Method with converting to string. Both time and space are O(n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]



# Method not converting to strings. Time is log(n) and space is O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        original, reverse  = x, 0

        while x != 0:
            reverse = reverse * 10 + x % 10
            x //= 10

        return original == reverse   

