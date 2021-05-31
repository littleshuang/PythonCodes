#!/bin/python3
# -*- coding: UTF-8 -*-

"""
请实现 copyRandomList 函数，复制一个复杂链表。
在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
"""



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


"""
1. 创建当前链表与复制链表交替出现的链表；
2. 遍历新链表，为复制后的链表的 random 赋值；
3. 遍历链表，将当前链表与复制后的链表分开。
"""


class Solution:
    def copy_random_list(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur_node = head
        cur_node = self.create_new_list(cur_node)
        cur_node = self.correct_random_value(cur_node)
        cur_node, new_node = self.split_list(cur_node)
        return new_node

    def create_new_list(self, head: 'Node') -> 'Node':
        node_a = head

        while node_a:
            node_b = Node(node_a.val, node_a.next, node_a.random)
            node_a.next = node_b
            node_a = node_b.next
        return head

    def correct_random_value(self, head: 'Node') -> 'Node':
        if not head or not head.next:
            return head
        node_b = head.next

        while node_b:
            if node_b.random is not None:
                node_b.random = node_b.random.next
            if node_b.next and node_b.next.next:
                node_b = node_b.next.next
            else:
                break
        return head

    def split_list(self, head: 'Node') -> ('Node', 'Node'):
        if not head:
            return None, None
        if not head.next:
            return head, None
        head_a, head_b = head, head.next
        node_a, node_b = head_a, head_b
        while node_b:
            node_a.next = node_b.next
            node_a = node_a.next
            if node_a and node_a.next:
                node_b.next = node_a.next
            node_b = node_b.next
        return head_a, head_b


def construct_list(node_list: ['Node']) -> 'Node':
    if not node_list:
        return None
    tmp_list = list()
    head = Node(node_list[0][0])
    node_a = head
    tmp_list.append(node_a)
    for i in range(1, len(node_list)):
        node_b = Node(node_list[i][0])
        node_a.next = node_b
        node_a = node_b
        tmp_list.append(node_a)

    node_a = head
    for item in node_list:
        if item[1] is not None:
            node_a.random = tmp_list[item[1]]
        node_a = node_a.next
    return head


if __name__ == "__main__":
    head_list = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = construct_list(head_list)
    head_b = Solution().copy_random_list(head)
    node_a = head_b
    while node_a:
        if node_a.random is None:
            print('[' + str(node_a.val) + ', None]')
        else:
            print('[' + str(node_a.val) + ', ' + str(node_a.random.val) + ']')
        node_a = node_a.next





