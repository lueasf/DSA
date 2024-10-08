# SUBSETS II
# SUBSETS AVEC DES DOUBLONS

# Un arbre dans lequel on prends un élément au moins une fois ou pas du tout, car on a des doublons.

# BYME
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        def dfs(index, curr):
            if index == len(nums):
                res.append(curr.copy())
                return
            else:
                curr.append(nums[index])
                dfs(index + 1, curr)
                curr.pop()

                while ( index + 1 < len(nums) and nums[index] == nums[index+1]):
                    index += 1
                dfs(index + 1, curr)
            return res
        return dfs(0, [])
    
print(Solution().subsetsWithDup([1,2,2]))