# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Rappel, les sets ne contiennent pas de doublons, on utilise cette structure de données.
# aussi appelé "Hash set" (calcule le hash de la valeur et les compares)

def containsDuplicate(nums):
    numset = set()
    for i in nums:
        if i in numset:
            return True
        else:
            numset.add(i)
    return False
