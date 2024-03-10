# Given an array of distinct integers candidates and a target integer 
# target, return a list of all unique combinations of candidates where 
# the chosen numbers sum to target. You may return the combinations in 
# any order. The same number may be chosen from candidates an 
# unlimited number of times. 

# Depth-First Search (DFS) approach.

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]


def combinationSum(candidates, target):
    output = [] # var de retour
    def dfs(i, curr, total): 
        if total == target: # cas de base, on ajoute le res partiel a la liste
            output.append(curr.copy())
            return #on renvoie None pour la fin de l'arbre récursif
        if i >= len(candidates) or total > target: #qs on a parcouru ts les nb ou c'est trop 
            return #on stop
        curr.append(candidates[i]) #on ajoute a un res partiel le premier nb
        dfs(i, curr, total + candidates[i]) #encore dfs pour voir si c'est possible de rajouter le mm nb
        curr.pop() # ça va faire plusieurs appel réc, la on veut changer de nb, on l'enleve et
        dfs(i + 1, curr, total) # on va tester avec les autres
    dfs(0, [], 0) # on commence par : le nb est me premier, le total vaut 0 et on a pas de sol partielle
    return output

# Le tout est un arbre

print(combinationSum([2,3,6,7],7))
