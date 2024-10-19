# Combination Sum : Amazon

# Depth-First Search (DFS) ou Parcours en profondeur.
# DFS est l'algo de base pour résoudre des problèmes de combinaisons et de permutations.

# Comme on peut avoir des doublons, on fait un arbre : "on prends ce nb, ou on prends pas ce nb"
# [] -> [1] et [] -> [], [1] -> [1,2] et [1] -> [1], [1,2] -> [1,2,2] et [1,2] -> [1,2] etc

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]

# FAV

# BYME
def combinationSum(candidates, target):
    res = []

    def dfs(curr,index, tot):
        if tot == target:
            res.append(curr[:])
            return
        if tot > target or index >= len(candidates):
            return 
        else:
            curr.append(candidates[index])
            dfs(curr, index + 1, tot + candidates[index]) # ca peut etre le mm chiffre
            curr.pop()
            dfs(curr, index + 1, tot) # pas forcement
        return res

    return dfs([], 0, 0)            
