#!/bin/python3
# -*- coding: UTF-8 -*-

"""
输入两个链表，找出它们的第一个公共节点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_intersect_node_len(head_a, head_b):
    if not head_a or not head_b:
        return None

    len_a, len_b = 0, 0
    node_a, node_b = head_a, head_b

    while node_a:
        len_a = len_a + 1
        node_a = node_a.next

    while node_b:
        len_b = len_b + 1
        node_b = node_b.next

    node_a, node_b = head_a, head_b
    if len_a > len_b:
        for i in range(len_a - len_b):
            node_a = node_a.next
    elif len_b > len_a:
        for i in range(len_b - len_a):
            node_b = node_b.next

    while node_a:
        if node_a == node_b:
            return node_a
        node_a = node_a.next
        node_b = node_b.next
    return None


def get_intersect_node_pointer(head_a, head_b):
    if not head_a or not head_b:
        return None

    node_a, node_b = head_a, head_b

    while node_a != node_b:
        if node_a:
            node_a = node_a.next
        else:
            node_a = head_b
        if node_b:
            node_b = node_b.next
        else:
            node_b = head_a
    return node_a


def construct_nodes(num_list, head_c):
    head_node = ListNode(num_list[0])

    next_node_1, next_node_2 = head_node, ListNode(num_list[1])
    next_node_1.next = next_node_2
    num_list.remove(num_list[0])
    num_list.remove(num_list[0])
    for i in num_list:
        next_node_1 = next_node_2
        next_node_2 = ListNode(i)
        next_node_1.next = next_node_2

    if head_c:
        next_node_2.next = head_c

    return head_node


def print_node_list(head):
    if not head:
        return

    node = head

    print("\n==========")
    while node:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    list_a = [4, 1]
    list_b = [5, 0, 1]
    list_c = [8, 4, 5]
    head_node_c = construct_nodes(list_c, None)
    head_node_a = construct_nodes(list_a, head_node_c)
    head_node_b = construct_nodes(list_b, head_node_c)

    print_node_list(head_node_a)
    print_node_list(head_node_b)

    intersect_node = get_intersect_node_len(head_node_a, head_node_b)
    # intersect_node = get_intersect_node_pointer(head_node_a, head_node_b)

    if not intersect_node:
        print("intersect node is None")
    else:
        print_node_list(intersect_node)


