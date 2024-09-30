# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
# the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

def productExcept(nums):
    length = len(nums)
    output = [1] * length
    for i in range(1,length):
        output[i] = output[i-1]*nums[i-1]

    right = nums[-1]
    for i in range(length - 2, -1, -1):
        output[i] *= right 
        right *= nums[i]
    return output

#BYME
def productExcept2(nums):
    output = []
    for i in range(len(nums)):
        a = 1
        for j in range(len(nums)):
            if (i !=j):
                a *= nums[j]
        output.append(a)
    return output

print(productExcept([1,2,3,4]))