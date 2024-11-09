# linéaire en temps et espace

class Solution:
    def getMaximumXor(self, nums: list[int], maximumBit: int) -> list[int]:
        mask = (1 << maximumBit) - 1
        res = [0] * len(nums)
        curr = 0
        
        for i in range(len(nums)):
            curr ^= nums[i] # ^ est l'op xor.
            res[len(nums)-i-1] = ~curr & mask # ~ inverse les bits
            
        return res
