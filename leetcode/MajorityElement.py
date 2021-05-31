#!/bin/python3
# -*- coding: UTF-8 -*-

"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
"""


def majority_element_1(nums):
    if not nums or len(nums) == 0:
        return None

    num_count = {}
    for num in nums:
        if num in num_count.keys():
            num_count[num] = num_count[num] + 1
        else:
            num_count[num] = 1
    part_count = len(nums) / 2

    for num, count in num_count.items():
        if count >= part_count:
            return num

    return None


def majority_element_2(nums):
    if not nums or len(nums) == 0:
        return None

    flag = 0
    majority_num = nums[0]

    for num in nums:
        if flag == 0:
            majority_num = num
        if num == majority_num:
            flag += 1
        else:
            flag -= 1
    return majority_num


if __name__ == "__main__":
    a_list = []
    b_list = [1, 3, 4, 2, 2, 2, 2]
    c_list = [1, 2, 3, 2, 4, 2, 2]

    majority_num_1_a = majority_element_1(a_list)
    majority_num_1_b = majority_element_1(b_list)
    majority_num_1_c = majority_element_1(c_list)

    majority_num_2_a = majority_element_2(a_list)
    majority_num_2_b = majority_element_2(b_list)
    majority_num_2_c = majority_element_2(c_list)

    print("majority_element_1(a_list): " + str(majority_num_1_a) if majority_num_1_a else "")
    print("majority_element_1(b_list): " + str(majority_num_1_b) if majority_num_1_b else "")
    print("majority_element_1(c_list): " + str(majority_num_1_c) if majority_num_1_c else "")

    print("majority_element_2(a_list): " + str(majority_num_2_a) if majority_num_2_a else "")
    print("majority_element_2(b_list): " + str(majority_num_2_b) if majority_num_2_b else "")
    print("majority_element_2(c_list): " + str(majority_num_2_c) if majority_num_2_c else "")


