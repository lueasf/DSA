# dichotomie:

# BYME

def search(self, nums, target: int) -> int:
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1

print(search([-1,0,3,5,9,12], 9))