#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time        : 2021/9/13 5:20 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 617-深度 or 深度优先搜索（合并二叉树）simple.py

'''
617. 合并二叉树
https://leetcode-cn.com/problems/merge-two-binary-trees
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def megerTrees(self, root1: TreeNode, root2: TreeNode):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val = root1.val + root2.val
        root1.left = self.megerTrees(root1.left, root2.left)
        root2.right = self.megerTrees(root2.right, root2.right)
        return root1
