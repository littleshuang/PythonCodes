#!/bin/python3
# -*- coding: UTF-8 -*-

"""
链表中倒数第K个节点

输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。
这个链表的倒数第3个节点是值为4的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
"""


class ListNode:
    def __init__(self, num):
        self.val = num
        self.next = None
        print(num)

    def set_val(self, num):
        self.val = num

    def set_next(self, node):
        self.next = node

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next


class Solution:
    def get_kth_from_end(self, head: ListNode, k: int) -> ListNode:
        if not head or k < 1:
            return head

        fast_node, slow_node = head, head
        count = 1
        while fast_node:
            fast_node = fast_node.get_next()
            count = count + 1
            if count > k:
                break
        if count <= k:
            return None

        while fast_node:
            fast_node = fast_node.get_next()
            slow_node = slow_node.get_next()

        return slow_node


def construct_nodes():
    head_node = ListNode(1)

    next_node_1, next_node_2 = head_node, ListNode(2)
    next_node_1.set_next(next_node_2)
    for i in range(3, 6):
        next_node_1 = next_node_2
        next_node_2 = ListNode(i)
        next_node_1.set_next(next_node_2)

    return head_node


if __name__ == "__main__":

    ret_node = Solution().get_kth_from_end(construct_nodes(), 3)
    print("===========")
    while ret_node:
        print(ret_node.get_val())
        ret_node = ret_node.get_next()
