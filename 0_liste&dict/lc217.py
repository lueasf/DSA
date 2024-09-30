# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Rappel, les sets ne contiennent pas de doublons, on utilise cette structure de données.
# aussi appelé "Hash set" (calcule le hash de la valeur et les compares)


#BYME 
def containsDuplicate(nums):
    numset = set()
    for i in nums:
        if i in numset:
            return True
        else:
            numset.add(i)
    return False

#BYME
def containsDuplicate2(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if (nums[i]==nums[i+1]):
            return True
    return False
