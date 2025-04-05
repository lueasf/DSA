

# BYME
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else :
            l = self.maxDepth(root.left)
            g = self.maxDepth(root.right)
            return max(l,g) + 1