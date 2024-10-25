# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def replaceValueInTree(self, root): 
        dic={} # dico pour stocker les valeurs des noeuds
        lev={} # dico pour stocker les valeurs des noeuds par niveau
        def traverse(root,level,oldroot,flag):
            if root: 
                if flag==0 and level>1: 
                    dic[oldroot] = dic.get(oldroot,0) + root.val # 
 
                    lev[level] = lev.get(level,0) + root.val
                
                elif flag==1:  
                    if level <= 1: root.val = 0
                    else: root.val = lev[level] - dic[oldroot]
                
                oldroot=root
                traverse(root.left,level+1,oldroot,flag)
                traverse(root.right,level+1,oldroot,flag)
        traverse(root,0,None,0) # on remplit le dico dic   
        traverse(root,0,None,1) # on remplit les valeurs des noeuds
        return root