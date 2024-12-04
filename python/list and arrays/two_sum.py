# TODO Given an array of integers nums and an integer target, return indices of the two numbers such that they add up
#  to target. You may assume that each input would have exactly one solution, and you may not use the same element
#  twice. You can return the answer in any order.

def two_sum(numbers: list, target: int) -> list | str:
    numbers_seen = {}

    for i, number in enumerate(numbers):
        complement = target - number
        if complement in numbers_seen:
            return [numbers_seen[complement], i]

        numbers_seen[number] = i
    return "No such combination of numbers"


print(two_sum([2, 7, 10, 8], 15))

"""
    Time and space complexity: O(n) because the algo can store all values from the list inside of number_seen 
    dictionary in worst scenario.
"""
