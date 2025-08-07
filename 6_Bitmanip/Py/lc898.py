# 1 solution in O(n)
from typing import List

def subarrayBitwiseORs(self, nums):
        result = set()
        prev = set() 
        
        for num in nums:
            curr = {num}
            for p in prev:
                curr.add(p | num)
            result.update(curr)
            prev = curr
        
        return len(result)


"""nums = [1, 2, 4]

# Index 0: num = 1
prev = {}
curr = {1}           # Subarray [1]
result = {1}
prev = {1}

# Index 1: num = 2  
prev = {1}
curr = {2}           # Subarray [2]
curr.add(1|2 = 3)    # Subarray [1,2]
curr = {2, 3}
result = {1, 2, 3}
prev = {2, 3}

# Index 2: num = 4
prev = {2, 3}
curr = {4}           # Subarray [4]
curr.add(2|4 = 6)    # Subarray [2,4]  
curr.add(3|4 = 7)    # Subarray [1,2,4]
curr = {4, 6, 7}
result = {1, 2, 3, 4, 6, 7}

in O(n)"""

#2 in O(n²)
def subarrayBitwiseORs(self, nums: List[int]) -> int:
        res = set()
        for i in range(len(nums)):
            curr_or = 0
            for j in range(i, len(nums)):
                curr_or |= nums[j]
                res.add(curr_or)

        return len(res)