#!/bin/python3
# -*- coding: UTF-8 -*-

"""
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，
则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。
如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi

测试用例：
"42" --> 42
"   -42" --> -42
"4193 with words" --> 4193
"words and 987" --> 0
"-91283472332" --> -2147483648
"""

"""
1. str 为空，return 0
2. str 第一个非空字符非数字，也非+-号，return 0
3. str 不含非空字符，return 0
4. str溢出，返回INT_MIN or INT_MAX
5. 若第一个非空字符为+、-号，读取从第二个字符开始到接下来的第一个非数字字符位置的字符，计算字符组成的数字
"""


class Solution:
    def my_atoi(self, s: str) -> int:
        if not s:
            return 0
        beg_index = self.find_beg(s)
        if beg_index == len(s):
            return 0
        if s[beg_index] != '+' and s[beg_index] != '-' and (s[beg_index] < '0' or s[beg_index] > '9'):
            return 0
        tag = 1
        if s[beg_index] == '-':
            tag = -1
            beg_index += 1
        elif s[beg_index] == '+':
            beg_index += 1

        num_end = beg_index
        for i in range(beg_index, len(s)):
            if s[i] < '0' or s[i] > '9':
                num_end = i
                break
            num_end += 1
        if num_end == beg_index:
            return 0
        return self.cal_num(s[beg_index:num_end], tag)

    def cal_num(self, s, tag):
        num = 0
        power = len(s) - 1
        INT_MIN = int(-pow(2, 31))
        INT_MAX = int(pow(2, 31) - 1)
        for c in s:
            num += int(c) * pow(10, power)
            power -= 1
        num = num * tag
        if num <= INT_MIN:
            return INT_MIN
        if num >= INT_MAX:
            return INT_MAX
        return num

    def find_beg(self, s):
        index = 0
        for c in s:
            if c != ' ':
                break
            index += 1
        return index


if __name__ == "__main__":
    str_list = ["42", "   -42", "4193 with words", "words and 987", "-91283472332"]

    for s in str_list:
        print("\nThe original str: " + s)
        num = Solution().my_atoi(s)
        print("The reversed num: " + str(num))
