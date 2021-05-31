#!/bin/python3
# -*- coding: UTF-8 -*-

"""
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
"""


def find_repeat_num(list_num):
    if not list_num:
        return -1

    res_list = list()
    for i in range(len(list_num)):
        res_list.append(-1)

    for i in list_num:
        if res_list[i] != -1:
            return i
        res_list[i] = 1
    return -1


if __name__ == "__main__":
    test_list = [1, 2, 4, 0, 3]
    k = find_repeat_num(test_list)
    print(k)
