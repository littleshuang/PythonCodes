#!/bin/python3
# -*- coding: UTF-8 -*-

"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof
"""


def validate_stack_sequences(pushed, popped):
    if not pushed and not popped:
        return True
    if not pushed or not popped:
        return False
    ia, ib = 0, 0
    stack = list()

    while True:
        if (len(stack) == 0 or stack[-1] != popped[ib]) and ia < len(pushed):
            stack.append(pushed[ia])
            ia += 1
        elif stack[-1] == popped[ib]:
            stack.pop()
            ib += 1
            if ib >= len(popped):
                return True
        elif ia >= len(pushed):
            return False
    return True
