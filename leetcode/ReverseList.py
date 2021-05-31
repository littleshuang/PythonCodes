#!/bin/python3
# -*- coding: UTF-8 -*-

"""
反转链表

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    if not head or not head.next:
        return head

    node_a, node_b = head, head.next
    head.next = None

    while node_b:
        node_c = node_b.next
        node_b.next = node_a
        node_a = node_b
        node_b = node_c

    return node_a


def construct_nodes(num_list):
    head_node = ListNode(num_list[0])

    next_node_1, next_node_2 = head_node, ListNode(num_list[1])
    next_node_1.next = next_node_2
    num_list.remove(num_list[0])
    num_list.remove(num_list[0])
    for i in num_list:
        next_node_1 = next_node_2
        next_node_2 = ListNode(i)
        next_node_1.next = next_node_2

    return head_node


if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5]
    head = construct_nodes(num_list)
    node = head
    print("The original list: ")
    while node:
        print(str(node.val))
        node = node.next
    reverse_head = reverse_list(head)

    reverse_node = reverse_head
    print("The reversed list: ")
    while reverse_node:
        print(str(reverse_node.val))
        reverse_node = reverse_node.next

