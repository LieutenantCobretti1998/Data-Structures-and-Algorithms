# TODO  Write a function called middle that takes a list and returns a new list that contains all
#  but the first and last elements.

def middle_function(elements: list) -> list:
    new_list = []

    for i in range(1, len(elements) - 1):
        new_list.append(elements[i])

    return new_list


print(middle_function([1, 2, 3, 5]))
