# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return None

        self.candidate = None
        self.max_dp = -1

        self.dfs(root, 0)

        return self.candidate

    def dfs(self, node, depth):
        if not node:
            return -1
        
        if not node.left and not node.right:
            if depth > self.max_dp:
                self.max_dp = depth
                self.candidate = node
            
            return depth
        
        l_dp = self.dfs(node.left, depth + 1)
        r_dp = self.dfs(node.righ, depth + 1)

        if l_dp == r_dp == self.max_dp:
            self.candidate = node

        return max(l_dp, r_dp)
    