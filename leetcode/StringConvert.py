#!/bin/python3
# -*- coding: UTF-8 -*-
"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
"""

"""
Steps:
1. 不同情况考虑:
    1.1 字符串s为空，返回s
    1.2 n<=1，返回s
    1.3 n=2
2. 计算列数
3. 将字符串存入二维数组中
4. 从二维数组中读取字符串
"""


class Solution:
    def convert(self, a_str: str, num: int) -> str:
        if not a_str or num <= 1 or len(a_str) <= num:
            return a_str

        ret_str = ""
        length = len(a_str)
        if num == 2:
            i = 0
            while i < length:
                ret_str += a_str[i]
                i += 2
            i = 1
            while i < length:
                ret_str += a_str[i]
                i += 2
            return ret_str

        tmp = int(length / (num*2 - 2))
        col = (1+(num-2))*tmp
        tmp2 = length % (num*2 - 2)
        if tmp2 == 0:
            pass
        elif tmp2 <= num:
            col = col + 1
        elif tmp2 > num:
            col = col + (tmp2 - num) + 1

        matrix = [[0 for i in range(col)] for j in range(num)]
        flag, row, col1, row1, i = False, num - 1, 0, -1, 0

        while i < length:
            if not flag:
                row1 += 1
                matrix[row1][col1] = a_str[i]
                if row1 >= row:
                    flag = True
            else:
                row1 -= 1
                col1 += 1
                matrix[row1][col1] = a_str[i]
                if row1 == 0:
                    flag = False
            i += 1

        ret_str = ""
        for i in range(num):
            for j in range(col):
                if matrix[i][j] != 0:
                    ret_str += matrix[i][j]

        return ret_str


if __name__ == "__main__":
    s = "LEETCODEISHIRING"
    print("\ns = LEETCODEISHIRING num = 2")
    print(Solution().convert(s, 2))

    print("\ns = LEETCODEISHIRING num = 3")
    print(Solution().convert(s, 3))

    print("\ns = LEETCODEISHIRING num = 4")
    print(Solution().convert(s, 4))

    print("\ns = LEETCODEISHIRING num = 5")
    print(Solution().convert(s, 5))

    print("\ns = LEETCODEISHIRING num = 6")
    print(Solution().convert(s, 6))

    print("\ns = LEETCODEISHIRING num = 7")
    print(Solution().convert(s, 7))

    print("\ns = LEETCODEISHIRING num = 8")
    print(Solution().convert(s, 8))

    print("\ns = LEETCODEISHIRING num = 9")
    print(Solution().convert(s, 9))

    print("\ns = LEETCODEISHIRING num = 10")
    print(Solution().convert(s, 10))

    print("\ns = LEETCODEISHIRING num = 11")
    print(Solution().convert(s, 11))

    print("\ns = LEETCODEISHIRING num = 12")
    print(Solution().convert(s, 12))

    print("\ns = LEETCODEISHIRING num = 13")
    print(Solution().convert(s, 13))

    print("\ns = LEETCODEISHIRING num = 14")
    print(Solution().convert(s, 14))

    print("\ns = LEETCODEISHIRING num = 15")
    print(Solution().convert(s, 15))

    print("\ns = LEETCODEISHIRING num = 16")
    print(Solution().convert(s, 16))
