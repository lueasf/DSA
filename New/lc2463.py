
from functools import cache # cache permet de stocker les résultats des appels précédents pour éviter de les recalculer


class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        
        @cache
        def dfs(i, j, k):
            if j == 0: 
                return 0
            if i == 0: 
                return float('inf')
            if k == 0: 
                if i == 1: 
                    return float('inf')
                return dfs(i - 1, j, factory[i - 2][1])             

            result1 = dfs(i - 1, j, factory[i - 2][1]) if i >= 2 else float('inf')
            result2 = dfs(i, j - 1, k - 1) + abs(robot[j - 1] - factory[i - 1][0])
            result = min(result1, result2)
            return result
                
        m, n = len(robot), len(factory)
        robot.sort()
        factory.sort()
        result = dfs(n, m, factory[n - 1][1])
        return result