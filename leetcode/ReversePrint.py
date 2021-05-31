#!/bin/python3
# -*- coding: UTF-8 -*-

"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_print(head):
    if not head:
        return list()

    ret_list = list()
    reverse_get(head, ret_list)
    return ret_list


def reverse_get(head, alist):
    if not head:
        return -1

    if head.next:
        reverse_get(head.next, alist)
    alist.append(head.val)


def construct_nodes():
    head_node = ListNode(1)

    next_node_1, next_node_2 = head_node, ListNode(2)
    next_node_1.next = next_node_2
    for i in range(3, 6):
        next_node_1 = next_node_2
        next_node_2 = ListNode(i)
        next_node_1.next = next_node_2

    return head_node


if __name__ == "__main__":
    con_node = construct_nodes()

    ret_node = reverse_print(con_node)
    print(ret_node)
