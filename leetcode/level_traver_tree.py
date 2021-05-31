#!/bin/python3
# -*- coding: UTF-8 -*-

"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def a(self):
        self.b()

    def b(self):
        print("b")


def traver_tree(root):
    h = 0
    tree_map = {}
    traver_tree_1(root, h, tree_map)
    return [item for item in tree_map.values()]


def traver_tree_1(root, h, tree_map):
    if not root:
        return
    if h in tree_map.keys():
        tree_map[h].append(root.val)
    else:
        tree_map[h] = [root.val]

    if root.left:
        traver_tree_1(root.left, h+1, tree_map)
    if root.right:
        traver_tree_1(root.right, h + 1, tree_map)


def construct_tree():
    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(5)
    node4 = TreeNode(4)
    node5 = TreeNode(15)
    node6 = TreeNode(7)
    node7 = TreeNode(1)
    node8 = TreeNode(8)
    node9 = TreeNode(6)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    node3.left = node7
    node4.left = node8
    node4.right = node9
    return root


if __name__ == "__main__":
    root = construct_tree()
    tree_map = traver_tree(root)
    print(tree_map)