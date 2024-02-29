# Given an integer array nums and an integer k, return the k most frequent elements. 

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

def topKFrequen(nums, k):
    occ = {}
    for i in nums:
        if i in occ:
            occ[i] += 1
        else:
            occ[i] = 1
    output = []
    for i in range(k):
        l=(max(occ, key=occ.get))
        output.append(l)
        occ[l] = 0
    return output

print(topKFrequen([1,1,1,2,2,2,4,3,4,2,7,9], 4))