#TODO check for permutation

def permutation(list_of_values1: list, list_of_values2: list) -> bool:
    if len(list_of_values1) != len(list_of_values2):
        return False
    list_of_values1.sort()
    list_of_values2.sort()
    return True if list_of_values1 == list_of_values2 else False


print(permutation([1, 2, 3, 4], [1, 2, 4, 5]))