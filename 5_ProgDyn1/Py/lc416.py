from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        
        dp = set()
        dp.add(0)

        for i in range(len(nums -1, -1, -1)):
            dp2 = set()
            for n in dp:
                if (nums[i] + n) == target:
                    return True
                dp2.add(nums[i] + n)
                dp2.add(n)
            dp = dp2
        
        return target in dp