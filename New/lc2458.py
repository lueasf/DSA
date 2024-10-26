# Height of Binary Tree After Subtree Removal Queries

from functools import lru_cache
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root, queries):
        @lru_cache(None) # Cette ligne permet de stocker les valeurs de la fonction height pour ne pas les recalculer à chaque fois
        def height(node):
            if not node:
                return -1

            return 1 + max(height(node.left),height(node.right))

        dict1 = collections.defaultdict(int) # dico qui renvoie une val par défaut si la clé n'existe pas
        def dfs(node,depth,max_val):
            if not node: return 

            dict1[node.val] = max_val

            dfs(node.left,depth+1,max(max_val,depth+1+height(node.right)))
            dfs(node.right,depth+1,max(max_val,depth+1+height(node.left)))

        dfs(root,0,0)

        return [dict1[i] for i in queries]