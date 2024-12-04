# TODO Write a function to remove the duplicate numbers on given integer array/list.

def dublicate_numbers(numbers: list) -> list:
    return list(set(numbers))


print(dublicate_numbers([1, 2, 3, 4, 5, 5, 2, 1, 1, 1]))

"""
    Space and time complexity is O(n) as list conversion is O(n) time complexity as well as set method.
    Space complexity is  O(m) as it depends list is have all unique values or not. In worst scenario is O(n) when number
    of list are equal to the number of values in set
"""