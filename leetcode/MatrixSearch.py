#!/bin/python3
# -*- coding: UTF-8 -*-

"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
"""


def find_number_in_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if matrix is None or len(matrix) <= 0 or len(matrix[0]) <= 0:
        return False
    # return find_number_recursion(matrix, target, 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
    return find_number_cycle(matrix, target)


def find_number_recursion(matrix, target, row_begin, row_end, col_beg, col_end):
    if matrix is None or len(matrix) == 0:
        # return -1, -1
        return False

    if row_begin > row_end or col_beg > col_end:
        # return -1, -1
        return False

    if target < matrix[row_begin][col_end]:
        return find_number_recursion(matrix, target, row_begin, row_end, col_beg, col_end - 1)
    elif target == matrix[row_begin][col_end]:
        # return row_begin, col_end
        return True
    else:
        return find_number_recursion(matrix, target, row_begin + 1, row_end, col_beg, col_end)


def find_number_cycle(matrix, target):
    if matrix is None or len(matrix) <= 0 or len(matrix[0]) < 0:
        return False

    row = len(matrix)-1
    col = len(matrix[0])-1
    i = 0
    j = col
    while i <= row and j >= 0:
        if target < matrix[i][j]:
            j = j - 1
        elif target == matrix[i][j]:
            return True
        else:
            i = i + 1
    return False


if __name__ == "__main__":
    test_matrix = [[1,   4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22],
                   [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]

    result_5 = find_number_in_matrix(test_matrix, 5)
    result_20 = find_number_in_matrix(test_matrix, 20)
    print("The result of 5: " + str(result_5))
    print("The result of 20: " + str(result_20))
