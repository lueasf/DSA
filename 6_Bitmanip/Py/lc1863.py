from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []

        def dfs(start, arr, l):
            x = 0
            for i in l:
                x ^= i
            res.append(x)

            for i in range(start, len(arr)):
                l.append(arr[i])
                dfs(i+1, arr, l)
                l.pop()

        dfs(0, nums, [])
        return sum(res)
    
    