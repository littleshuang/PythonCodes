#!/bin/python3
# -*- coding: UTF-8 -*-

"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
"""


def replace_space(str_to_replace):
    if not str_to_replace:
        return str_to_replace

    str_replaced = ""
    for ch in str_to_replace:
        if ch == " ":
            ch = '%20'
        str_replaced = str_replaced + ch
    return str_replaced


if __name__ == "__main__":
    print(replace_space("We are happy!"))
