#Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# The intuition behind this solution is to use a two-pointer approach 
# to find a pair of numbers in the sorted array that sums up to the target value.

def twoSum(numbers, target):
    l,r = 0, len(numbers)-1 # pointing ton start and end of the array
    while l<r:
        sum_v = numbers[l] + numbers[r]
        if sum_v > target:
            r -=1
        elif sum_v < target:
            l+=1
        else:
            return  [l+1, r+1]       

print(twoSum([2,7,11,15], 9))