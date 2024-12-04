#TODO Given an integer array nums, return true
# if any value appears at least twice in the array, and return false if every element is distinct.

def contains_dublicate(arr: list) -> bool:
    seen = set()
    for num in arr:
        if num not in seen:
            seen.add(num)
        elif num in seen:
            return True
    return False


print(contains_dublicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))


"""
    Time and space complexity: O(n) in worst case for space complexity scenario 
    when set will be in the same size as the origin list/array
"""