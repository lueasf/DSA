# Top K frequent elements : Amazon

# Given an integer array nums and an integer k, return the k most frequent elements. 

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

def topKFrequent(nums, k):
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

#BYME
def topKFrequent(nums, k):
    dico = dict()
    L = []
    O = []
    for i in range(len(nums)):
        if nums[i] not in dico:
            dico[nums[i]] = 1
        else :
            dico[nums[i]] +=1
    for key, value in dico.items():
        L.append((value, key))
    L.sort(reverse=True)

    for i in range(k):
        O.append(L[i][1])
    
    return O

print(topKFrequent([1,1,1,2,2,2,4,3,4,2,7,9], 4))