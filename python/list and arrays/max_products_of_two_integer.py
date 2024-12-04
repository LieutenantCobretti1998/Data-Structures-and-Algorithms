# TODO Find the maximum product of two integers in an array where all elements are positive.

def max_products_of_two(integers: list) -> int:
    integers.sort(reverse=True)
    return integers[0] * integers[1]


print(max_products_of_two([1, 2, 3, 4, 60]))

# This is just a sort version with using built in functions


"""Linear search"""


def max_products_of_two(integers: list) -> int | None:
    if len(integers) < 2:
        return None
    max1 = max(integers[0], integers[1])
    max2 = min(integers[0], integers[1])

    for number in integers[2:]:
        if number > max1:
            max2 = max1
            max1 = number
        elif number > max2:
            max2 = number
    return max1 * max2


print(max_products_of_two([60, 2, 3, 3, 4]))

"""
    Time Complexity: O(n) because it only requires a single pass through the array.
    Space Complexity: O(1) since only a fixed number of variables are used, regardless of the input size.
"""