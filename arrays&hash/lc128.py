# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2,3]
# Output: 4

def longestConsecutive(nums):
    if nums == []:
        return 0
    nums2 = sorted(set(nums))
    compt = 1
    lico = []
    for i in range(1,len(nums2)):
        if abs(nums2[i-1] - nums2[i]) == 1:
            compt += 1
        else:
            lico.append(compt)
            compt = 1
        lico.append(compt)
    return max(lico)

print(longestConsecutive([100,4,200,1,3,2]))