#TODO ou are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    rotated = list(reversed(list(zip(*matrix))))
    return rotated


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
