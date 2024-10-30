from bisect import bisect_left # cette fonction permet de trouver la position d'insertion d'un élément dans une liste triée
# exemple: bisect_left([1, 2, 3, 4, 5], 3) retourne 2

# Longest Increasing Subsequence (LIS) Solution from both directions

class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        size = len(nums)
        left = [0] * size
        right = [0] * size
         
        dp = []  
        for i in range(size):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
            left[i] = len(dp)
         
        dp = []  
        for i in range(size - 1, -1, -1):
            idx = bisect_left(dp, nums[i])
            if idx == len(dp):
                dp.append(nums[i])
            else:
                dp[idx] = nums[i]
            right[i] = len(dp)
        
        minRemove = size
        for i in range(size):
            if left[i] > 1 and right[i] > 1:
                minRemove = min(minRemove, size - left[i] - right[i] + 1)
        
        return minRemove