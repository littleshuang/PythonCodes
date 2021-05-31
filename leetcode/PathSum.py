#!/bin/python3
# -*- coding: UTF-8 -*-

"""
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def path_sum(self, root: TreeNode, sum: int) -> [[int]]:
        if not TreeNode:
            return []
        tmp_sum = 0
        alist = list()
        return self.cal_path(root, sum, tmp_sum, alist)

    def cal_path(self, root: TreeNode, sum: int, tmp_sum: int, alist: [int]):
        if not root:
            return
        node = root
        tmp_sum += node.val
        alist.append(node.val)
        blist = list()

        if tmp_sum == sum and not node.left and not node.right:
            blist.append(alist.copy())

        if node.left:
            l_list = self.cal_path(node.left, sum, tmp_sum, alist)
            if len(l_list) > 0:
                blist.extend(l_list)
        if node.right:
            r_list = self.cal_path(node.right, sum, tmp_sum, alist)
            if len(r_list) > 0:
                blist.extend(r_list)
        sum -= node.val
        del alist[-1]
        return blist


def construct_tree(alist, beg):
    if not alist or beg < 0:
        return None
    if beg >= len(alist):
        return
    a_node = TreeNode(alist[beg])
    if beg*2+1 < len(alist):
        a_node.left = construct_tree(alist, beg*2+1)
    if beg*2+2 < len(alist):
        a_node.right = construct_tree(alist, beg*2+2)
    return a_node


def construct_tree_1():
    head = TreeNode(5)
    node_1 = head
    node_2 = TreeNode(4)
    node_3 = TreeNode(8)
    node_4 = TreeNode(11)
    node_5 = TreeNode(13)
    node_6 = TreeNode(4)
    node_7 = TreeNode(7)
    node_8 = TreeNode(2)
    node_9 = TreeNode(5)
    node_10 = TreeNode(1)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_3.left = node_5
    node_3.right = node_6
    node_4.left = node_7
    node_4.right = node_8
    node_6.left = node_9
    node_6.right = node_10
    node_8.left = TreeNode(0)
    node_9.left = TreeNode(0)
    return head


def construct_2():
    head = TreeNode(-2)
    head.right = TreeNode(-3)
    return head


def print_node(node):
    if not node:
        return
    print(node.val)
    if node.left:
        print_node(node.left)
    if node.right:
        print_node(node.right)


if __name__ == "__main__":
    head = construct_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1], 0)
    head_1 = construct_tree_1()
    # node = head
    # print_node(node)
    ret_list = Solution().path_sum(head_1, 22)
    if not ret_list:
        print('ret_list is None')
    else:
        print(ret_list)

    head_2 = construct_2()
    ret_list = Solution().path_sum(head_2, -5)
    if not ret_list:
        print('ret_list is None')
    else:
        print(ret_list)

