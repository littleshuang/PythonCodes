#!/bin/python3
# -*- coding: UTF-8 -*-

"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_list(head_a, head_b):
    if not head_a:
        return head_b

    if not head_b:
        return head_a

    node_a, node_b = head_a, head_b
    head_c = ListNode(1)

    if node_a.val <= node_b.val:
        head_c = node_a
        node_a = node_a.next
    else:
        head_c = node_b
        node_b = node_b.next
    node_c = head_c

    while node_a and node_b:
        if node_a.val <= node_b.val:
            node_c.next = node_a
            node_c = node_c.next
            node_a = node_a.next
        else:
            node_c.next = node_b
            node_c = node_c.next
            node_b = node_b.next

    if node_a:
        node_c.next = node_a
    elif node_b:
        node_c.next = node_b
    return head_c


def construct_nodes(num_list):
    if not num_list or len(num_list) == 0:
        return None

    if len(num_list) == 1:
        return ListNode(num_list[0])

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


def print_node_list(head):
    if not head:
        return

    node = head

    print("\n==========")
    while node:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    a_list = [1, 2]
    b_list = [1, 3, 4]
    a_head = construct_nodes(a_list)
    b_head = construct_nodes(b_list)

    print_node_list(a_head)
    print_node_list(b_head)
    c_head = merge_two_list(a_head, b_head)
    d_head = merge_two_list(None, None)
    print_node_list(a_head)
    print_node_list(b_head)
    print_node_list(c_head)
    print_node_list(d_head)
