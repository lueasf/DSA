# Two Sum II : Amazon

#Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# The intuition behind this solution is to use a two-pointer approach 
# to find a pair of numbers in the sorted array that sums up to the target value.

# FAV 

#BYME
def twoSum(numbers, target):
    l,r = 0, len(numbers) - 1
    while l<r :
        if (numbers[l]+numbers[r] == target):
            return [l+1,r+1]
        elif (numbers[l]+numbers[r] < target):
            l+=1
        else:
            r-=1
    return []
    
#BETTER
def twoSum2(numbers, target):
    vu = {}
    for i in range(len(numbers)):
        diff = target - numbers[i]
        if diff in vu:
            return [vu[diff] + 1, i +1]
        else:
            vu[numbers[i]] = i

print(twoSum([2,7,11,15], 9))
print(twoSum2([2,7,11,15], 9))