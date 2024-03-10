# meme pb que le 39, sauf que la chaque nombre doit etre utilisé au plus 1 fois dans une solution partielle

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# output = [[1,1,6],[1,2,5],[1,7],[2,6]]

def combinationSum2(candidates, target):
    candidates.sort()
    res = []
    def backtrack(position, cur, target): # i cur target
        if target == 0:
            res.append(cur.copy())
        if target <= 0:
            return        
        prev = -1
        for i in range(position, len(candidates)):
            if candidates[i] == prev:
                continue
            cur.append(candidates[i])
            backtrack(i+1, cur, target - candidates[i])
            cur.pop()
            prev = candidates[i]

    backtrack(0,[], target)
    return res

print(combinationSum2([10,1,2,7,6,1,5], 8))