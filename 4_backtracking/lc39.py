# Depth-First Search (DFS) ou Parcours en profondeur.
# DFS est l'algo de base pour résoudre des problèmes de combinaisons et de permutations.

# Comme on peut avoir des doublons, on fait un arbre : "on prends ce nb, ou on prends pas ce nb"
# [] -> [1] et [] -> [], [1] -> [1,2] et [1] -> [1], [1,2] -> [1,2,2] et [1,2] -> [1,2] etc

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]

# BYME
def combinationSum(candidates, target):
    res = []
    def dfs(index, comb, total):
        if total == target:
            res.append(comb.copy())
            return
        if total > target or index >= len(candidates):
            return
        else :
            comb.append(candidates[index])
            dfs(index, comb, total + candidates[index])
            comb.pop()
            dfs(index + 1, comb, total)
        return res
    
    return dfs(0, [], 0)

print(combinationSum([2,2,3],8))
