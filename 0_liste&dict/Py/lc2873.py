from typing import List


def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        L = [0]*n
        R = [0]*n
        for i in range(n - 1):
            L[i+1] = max(L[i], nums[i])
            R[n - 2 - i] = max(R[n - 1 - i], nums[n - 1 - i])
        return max(0,max((L[i] - nums[i])*R[i] for i in range(1, n - 1)))

# We compute the maximum value from the left and right sides of each element in the list.
