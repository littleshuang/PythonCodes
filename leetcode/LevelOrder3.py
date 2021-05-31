#!/bin/python3
# -*- coding: UTF-8 -*-

"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def level_order(self, root: TreeNode) -> [[int]]:
        if not root:
            return []

        alist, blist = list(), list()
        ret_list = list()
        alist.append(root)
        while True:
            if len(alist) > 0:
                tmp_list = list()
                node = alist.pop()
                while node:
                    tmp_list.append(node.val)
                    if node.left:
                        blist.append(node.left)
                    if node.right:
                        blist.append(node.right)
                    if len(alist) > 0:
                        node = alist.pop()
                    else:
                        ret_list.append(tmp_list)
                        break
            elif len(blist) > 0:
                tmp_list = list()
                node = blist.pop()
                while node:
                    tmp_list.append(node.val)
                    if node.right:
                        alist.append(node.right)
                    if node.left:
                        alist.append(node.left)
                    if len(blist) > 0:
                        node = blist.pop()
                    else:
                        ret_list.append(tmp_list)
                        break
            else:
                break
        return ret_list

