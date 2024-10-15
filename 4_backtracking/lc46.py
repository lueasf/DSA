# donner les permutations 

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# mieux
# https://www.youtube.com/watch?v=gFm1lEfnzUQ
def prmute(self, nums):
    n = len(nums)
    res = []
    sol = [] # partial sol

    def dfs():
        if len(sol) == n:
            res.append(sol[:])
            return
        
        for x in nums:
            if x not in sol:
                sol.append(x)
                dfs()
                sol.pop()
    dfs()
    return res

# DFS 
# Faire un arbre dans lequel on va permuter chaque element avec tous les autres 1 fois.
# Cela ne créera pas de doublons.
def permute(nums):
    res = []

    def dfs(index):
        if index == len(nums):
            res.append(nums.copy())
            return
        else:
            for i in range(index, len(nums)): # attention boucle commence a index
                nums[index], nums[i] = nums[i], nums[index]
                
                dfs(index+1)
                nums[index], nums[i] = nums[i], nums[index]
    dfs(0)
    return res

print(permute([1,2,3]))


# quand on regardde l'arbre, le premier niveau c'est qd i =0, 1 et 2
#                        [1, 2, 3]
#                /        |                    \
#       [1, 2, 3] [2, 1, 3]                 [3, 2, 1]
#        /   \           /   \                  /   \
# [1, 2, 3] [1, 3, 2] [2, 1, 3] [2, 3, 1] [3, 2, 1] [3, 1, 2]


# dfs(0) -> i = 0, index = 0 (liste: [1, 2, 3])
#     dfs(1) -> i = 1, index = 1 (liste: [1, 2, 3])
#         dfs(2) -> i = 2, index = 2 (liste: [1, 2, 3])
#             dfs(3) -> index = 3 (ajout de [1, 2, 3] dans res)



# https://www.youtube.com/watch?v=s7AvT7cGdSo
def permte(self, nums):
    res = []

    if (len(nums)==1):
        return [nums[:]]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = self.permte(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)
    return res

