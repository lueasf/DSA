# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2,3]
# Output: 4

#BYME
def longestConsecutive(nums):
        if nums == []:
            return 0
        L = []
        count = 1
        nums.sort()
        for i in range(1,len(nums)):
            if ((nums[i]-nums[i-1])==1):
                count += 1
            elif (nums[i] == nums[i-1]):
                continue
            else:
                L.append(count)
                count = 1
        L.append(count)
        return max(L)

print(longestConsecutive([100,4,200,1,3,2]))