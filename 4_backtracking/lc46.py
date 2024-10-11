# donner les permutations 

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

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
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                dfs(index+1)
                nums[index], nums[i] = nums[i], nums[index]
        return res
    return dfs(0)

print(permute([1,2,3]))

# LC

