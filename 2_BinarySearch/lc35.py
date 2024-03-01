# trouver l'index de qqch dans une liste triée et supposer sinon

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            n = nums.index(target)
            return n
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums) 
        else:
            for i in range(len(nums)-1):
                if nums[i] < target < nums[i+1]:
                    return i + 1