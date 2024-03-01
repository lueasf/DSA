# dichotomie:

def search(nums, target):
    l,r = 0, len(nums)-1
    while (l<=r):
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1

print(search([-1,0,3,5,9,12], 9))