#!/bin/python3
# -*- coding: UTF-8 -*-

"""
包含 min 函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数，
在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list_a = list()
        self.list_b = list()

    def push(self, x: int) -> None:
        self.list_a.append(x)

        if len(self.list_b) == 0:
            self.list_b.append(x)
        elif x <= self.list_b[-1]:
            self.list_b.append(x)

    def pop(self) -> None:
        top_num = self.top()

        if top_num <= self.list_b[-1]:
            self.list_b.pop()

        self.list_a.pop()

    def top(self) -> int:
        return self.list_a[-1]

    def min(self) -> int:
        return self.list_b[-1]

    def print_list(self):
        print("\n\n==========print_list========")
        for item in self.list_a:
            print(str(item))


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(2)
    minStack.push(3)
    minStack.push(0)
    minStack.push(5)
    minStack.push(-2)

    minStack.print_list()
    print("minStack top: " + str(minStack.top()))
    print("minStack min: " + str(minStack.min()))
    minStack.pop()
    minStack.print_list()
    print("minStack top: " + str(minStack.top()))
    print("minStack min: " + str(minStack.min()))
    minStack.pop()
    minStack.print_list()
    print("minStack top: " + str(minStack.top()))
    print("minStack min: " + str(minStack.min()))
    minStack.pop()
    minStack.print_list()
    print("minStack top: " + str(minStack.top()))
    print("minStack min: " + str(minStack.min()))
