# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain DUPLICATE triplets.

# https://www.youtube.com/watch?v=IIxoo93bmPQ

def threeSum(numbers):
    numbers.sort()
    res = []
    for i in range(len(numbers)-2):
        if numbers[i] > 0:
            break # on sort de la boucle car les autres sont sup à 0.
        if i > 0 and numbers[i] == numbers[i-1]:
            continue # on passe cette iteration
        l = i + 1
        r = len(numbers) -1
        while l < r:
            total = numbers[i] + numbers[l] + numbers[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                trip = [numbers[i], numbers[l], numbers[r]]
                res.append(trip)
                while l<r and numbers[l] == trip[1]:
                    l += 1
                while l<r and numbers[r] == trip[2]:
                    r -= 1
    return res
