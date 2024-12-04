#TODO Write a function to find all pairs of an integer array whose sum is equal to a given number.
# Do not consider commutative pairs.


def pair_sum(numbers: list, target: int) -> list:
    pairs = []
    seen = set()
    for i in range(len(numbers)):
        complement = target - numbers[i]
        if complement in seen:
            pairs.append((complement, numbers[i]))
        seen.add(numbers[i])

    return pairs


pairs = pair_sum([10, 15, 4, 10, 8, 1, 6, 1, -3, 2], 12)
print(pairs)

"""
    Due to for loop we got O(n) time complexity and O(n) space complexity in worst case scenario be equal to the list size
"""