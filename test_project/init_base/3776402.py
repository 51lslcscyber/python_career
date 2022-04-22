# !usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/20 21:45
# @version: 1.0.1
# Created by: Python3.9.6
# @author:鹄思鹄想bit森
# WARNING: run again.Do not edit this file unless you know what you are doing.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        return root


if __name__ == "__main__":
    print()
    pass