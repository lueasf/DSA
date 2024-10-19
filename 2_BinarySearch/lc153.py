# Min in a rotated sorted array : Facebook

# BYME (O(n))
def findMin(self, nums) -> int:
    n = len(nums)
    l,r = 0, n-1

    while l < r:
        m = (l+r)//2 # // pour avoir un int
        if nums[m] > nums[r]:
            l = m+1
        else:
            r = m
    return nums[l]