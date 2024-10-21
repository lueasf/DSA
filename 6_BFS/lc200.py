# Number of Islands : Google, Uber

# Problème de graphe
# Time : O(m*n)

# En gros on parcourt et des qu'on voit un 1, on le compte et tout ce qui est autour on le met a 0,
# puis on continue le parcous avec dsf.

# FAV

class Solution:
    def numIslands(self, grid) -> int:
        m, n = len(grid), len(grid[0])
 
        def dfs(i,j):
            if i < 0 or i >=m or j<0 or j >=n or grid[i][j] != "1":
                return 
            else:
                grid[i][j] = "0"
                dfs(i, j + 1) # right 
                dfs(i + 1, j) # down
                dfs(i, j - 1) # left
                dfs(i - 1, j) # up


        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)

        return res