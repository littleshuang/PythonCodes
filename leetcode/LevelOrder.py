#!/bin/python3
# -*- coding: UTF-8 -*-

"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def level_order(self, root: TreeNode) -> [int]:
        if not root:
            return []

        num_list = list()
        node_list = list()
        node = root
        while node:
            num_list.append(node.val)
            if node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)
            if len(node_list) > 0:
                node = node_list[0]
                del node_list[0]
            else:
                break
        return num_list


def construct_tree(num_list):
    if not num_list:
        return None
    node_list = list()
    for num in num_list:
        if num is None:
            node_list.append(None)
        else:
            node_list.append(TreeNode(num))

    i = 0
    head = node_list[0]
    while 2*i+2 < len(node_list):
        if node_list[2*i+1]:
            node_list[i].left = node_list[2*i+1]
        if node_list[2*i+2]:
            node_list[i].right = node_list[2*i+2]
        i += 1
    return head


def print_tree(root):
    node = root
    print(node.val)
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)


if __name__ == "__main__":
    head = construct_tree([3, 9, 20, None, None, 15, 7])
    node = head
    print_tree(node)
    node_list = Solution().level_order(head)



