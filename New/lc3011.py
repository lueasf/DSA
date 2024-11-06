class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        maxi = -1
        ind = 0
        for i in range(len(nums)):
            b = bin(nums[i]).count('1')
            if i > 0:
                if b != prev: 
                    maxi = max(nums[ind:i]) 
                    ind = i  
                if nums[i] < maxi:
                    return False
            prev = b
        return True