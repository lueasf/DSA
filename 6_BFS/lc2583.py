from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level = [root] 
        ans = [] 
        while level: 
            l = [] 
            n = 0
            for i in level: # pour chaque noeud du niveau actuel
                n += i.val # on ajoute la valeur du noeud à la somme
                if i.left: 
                    l.append(i.left) 
                if i.right:
                    l.append(i.right) 
            ans.append(n) 
            level = l 
        ans.sort() 
        if len(ans) >= k: 
            return ans[-k]
        return -1       