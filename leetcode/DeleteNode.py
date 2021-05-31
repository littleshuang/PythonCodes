#!/bin/python3
# -*- coding: UTF-8 -*-

"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(head, target):
    if not head:
        return None

    if head.val == target:
        head = head.next
        return head

    if not head.next:
        return head

    node_a, node_b = head, head.next

    while node_b:
        if node_b.val == target:
            node_a.next = node_b.next
            node_b = None
            break
        node_a = node_a.next
        node_b = node_b.next
    return head


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


def print_node_list(head):
    if not head:
        return

    node = head

    print("\n==========")
    while node:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    list_a = [4, 1, 8, 2, 5]
    node_a = construct_nodes(list_a)
    print_node_list(node_a)

    node_b = delete_node(node_a, 8)
    print_node_list(node_b)
