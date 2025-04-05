

# BYME

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional 

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def aux(root):
            if root is None:
                return root
            tmp = root.right
            root.right = root.left
            root.left = tmp
            aux(root.right)
            aux(root.left)
            return root

        return aux(root)
        