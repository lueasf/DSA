# backtracking

# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations. 
# Each number is used at most once.

# approche : on commence avec le premier
# on ajoute le premier, puis le deuxieme, puis etc, et quand on dépasse, on revient en arrière


def combinaisonSum3(k, n):
    nb = [i for i in range(1, 10)]
    output = []

    def dfs(i, curr, total):
        if total == n and len(curr) == k:
            output.append(curr.copy())
            return
        if i >= 9 or total > n:
            return
        for j in range(i, 9):
            curr.append(nb[j])
            dfs(j + 1, curr, total + nb[j])
            curr.pop() # pour [1,...] et ba on enleve 1 et donc hop en re rentrant dans la boucle on met 2 : [2,...]

    dfs(0, [], 0)
    return output, nb

print(combinaisonSum3(3,9))