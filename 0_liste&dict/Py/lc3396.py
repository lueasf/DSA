from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nb_op = 0
        while len(nums) > len(set(nums)):
            nums = nums[3:]
            nb_op += 1
        return nb_op
    

# The loop runs O(n) times in the worst case.
# Each iteration create a new set (O(n)) and slice the list (O(n)).
# The total time complexity is O(n^2).
# The space complexity is O(n) for the set.