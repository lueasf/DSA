# meme pb que le 39, sauf que la chaque nombre doit etre utilisé au plus 1 fois dans une solution partielle

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# output = [[1,1,6],[1,2,5],[1,7],[2,6]]

#utilisation d'un arbre de backtracking

# BYME
def combinationSum2(self, candidates, target: int):
    res = []
    candidates.sort()
    def dfs(index,curr,total):
        if total == target:
            res.append(curr.copy())
            return
        if total > target:
            return
        else:
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i -1]:
                    continue
                curr.append(candidates[i])
                dfs(i + 1, curr, total + candidates[i])
                curr.pop()
        return res
    return dfs(0,[],0)

print(combinationSum2([10,1,2,7,6,1,5], 8))