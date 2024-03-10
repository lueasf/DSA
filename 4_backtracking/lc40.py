# meme pb que le 39, sauf que la chaque nombre doit etre utilisé au plus 1 fois dans une solution partielle

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# output = [[1,1,6],[1,2,5],[1,7],[2,6]]

def combinationSum2(candidates, target):
    output = []
    def dfs(i, curr, total):
        if total == target:
            output.append(curr.copy())
            return
        if total > target:
            return
        curr.append(candidates[i])
        dfs( i and i!=j, curr, total + candidates[i])
    dfs(0,[],0)
    return output