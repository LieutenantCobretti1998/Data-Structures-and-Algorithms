
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0

        for i in range(len(s)):
            curr = roman_numbers[s[i]]
            next = roman_numbers[s[i + 1]] if i + 1 < len(s) else 0

            if curr < next:
                total -= curr
            else:
                total += curr

        return total

#     Time and Space complexity are O(n) and O(1)

