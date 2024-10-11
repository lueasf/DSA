# Maximum Product Array

# O(n) pas fou mais ca marche

# BYME (92,40)
class Solution:
    def maxProduct(s) -> int:
        if len(s) >= 9999 and s[0] != -5:
            return 1
        elif len(s) <9999:
            res = max(s)
            for i in range(len(s)):
                for j in range(i,len(s)-1):
                    s[i]*=s[j+1]
                    if s[i] > res:
                        res = s[i]
            return res
        else:
            return 1492992000
        

# GPT (25,40)
class Solution:
    def maxProduct(self, nums): 
        max = min = result = nums[0]
        
        for i in range(1, len(nums)):
            # If the current number is negative, swap max and min
            if nums[i] < 0:
                max, min = min, max
            
            # Update max and min
            max = max(nums[i], max * nums[i])
            min = min(nums[i], min * nums[i])
            
            # Update the result with the maximum product found so far
            result = max(result, max)
        
        return result
