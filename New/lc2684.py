# Dyn + DFS : 

# FAV

class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            res = 0
            for di, dj in [(-1, 1), (0, 1), (1, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    res = max(res, dfs(ni, nj) + 1)
            dp[i][j] = res
            return res

        return max(dfs(i, 0) for i in range(m))

