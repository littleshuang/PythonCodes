#!/bin/python3
# -*- coding: UTF-8 -*-

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
斐波那契数列：f(n)=f(n-1)+f(n-2)
"""


def num_ways(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2

    return num_ways(n-1) + num_ways(n-2)


def num_ways_1(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2

    num_list = list()
    num_list.append(1)
    num_list.append(2)

    m = n - 2
    for i in range(m):
        num_list.append(int(num_list[-1] + num_list[-2]) % (1e9+7))
    return int(num_list[n-1])


if __name__ == "__main__":
    print("5: " + str(num_ways(5)))
    print("2: " + str(num_ways(2)))
    print("10: " + str(num_ways(10)))
    # print("44: " + str(num_ways(44)))

    print("==========")
    print("3: " + str(num_ways_1(3)))
    print("2: " + str(num_ways_1(2)))
    print("78: " + str(num_ways_1(78)))
    print("44: " + str(num_ways_1(44)))
