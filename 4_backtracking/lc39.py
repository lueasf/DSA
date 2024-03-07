# Given an array of distinct integers candidates and a target integer 
# target, return a list of all unique combinations of candidates where 
# the chosen numbers sum to target. You may return the combinations in 
# any order. The same number may be chosen from candidates an 
# unlimited number of times. 

# Depth-First Search (DFS) approach.

def combinationSum(candidates, target):
    ouput = []
    def dfs(i, curr, total):
        if total == target:
            ouput.append(curr.copy())
            return
        if i >= len(candidates) or total > target:
            return
        curr.append(candidates[i])
        dfs( i , curr, total + candidates[i])
        curr.pop()
        dfs( i + 1, curr, total)
    dfs(0,[], 0)
    return ouput

print(combinationSum([2,3,5],8))