#!/bin/python3
# -*- coding: UTF-8 -*-

"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
"""


def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return list()

    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    ret_list = list()

    while left <= right and top <= bottom:
        ''' left to right '''
        for i in range(left, right + 1):
            ret_list.append(matrix[top][i])

        ''' top to bottom '''
        for i in range(top + 1, bottom + 1):
            ret_list.append(matrix[i][right])

        if left < right and top < bottom:
            ''' right to left '''
            for i in range(right - 1, left, -1):
                ret_list.append(matrix[bottom][i])

            ''' bottom to top '''
            for i in range(bottom, top, -1):
                ret_list.append(matrix[i][left])

        top = top + 1
        bottom = bottom - 1
        left = left + 1
        right = right - 1
    return ret_list


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    res = spiral_order(matrix)
    print(res)

