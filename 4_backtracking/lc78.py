# SUBSETS 

#Given an integer array nums of unique elements, return all possible subsets
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Arbre : on prends un élément ou pas du tout

# BYME
class Solution:
    def subsets(self, nums):
        res = []
        def backtrack(index, curr):
            if index == len(nums):
                res.append(curr.copy())
                return
            else:
                curr.append(nums[index])
                backtrack(index+1, curr)
                curr.pop()
                backtrack(index+1, curr)
            return res
        return backtrack(0,[])

# REP
def subsets(nums):
    def backtrack(first = 0, curr = []):
        if len(curr) == k:
            res.append(curr[:])
            return 
        for i in range(first,n):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()    
    res = []
    n = len(nums)
    for k in range(n + 1):
        backtrack()
    return res

print(subsets([1,2,3]))