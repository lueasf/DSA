# 1493. Longest Subarray of 1's After Deleting One Element - Medium

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zc = 0
        lg = 0
        start = 0
        
        for i in range(len(nums)):
            zc += (nums[i] == 0)
            
            while zc > 1:
                zc -= (nums[start] == 0)
                start += 1
            
            lg = max(lg, i - start)
        
        return lg