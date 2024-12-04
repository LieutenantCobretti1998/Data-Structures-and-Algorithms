# TODO: Write a function to find the missing number in a given integer array of 1 to 100. The function takes to
#  parameter the array and the number of elements that needs to be in array.  For example if we want to find missing
#  number from 1 to 6 the second parameter will be 6.

def missing_number(arr: list, max_num: int) -> int:
    expected_sum = max_num * (max_num + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


print(missing_number([1, 3, 4,  5, 6], 6))

"""
    Time is O(N) and space complexity is O(1) for this algorithm. The base arithemtic was used here when for expected 
    sum we formula  of max_num * (max_num + 1) // 2
"""
