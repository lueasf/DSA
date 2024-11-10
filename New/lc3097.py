
# Sliding Window
# not a O(n²) bruteforce sol but a O(n) sol for time and O(1) for space

class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        res = float("inf") 
        bits = [0] * 32
        left_p = 0

        def bits_update(bits, n, diff): # when we put or remove a number, we turn off the 1 bits from the OR.
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff

        def bits_to_int(bits): # Tab to int
            res = 0
            for i in range(32):
                if bits[i]:
                    res += (1 << i)
            return res

        for r in range(len(nums)):
            bits_update(bits, nums[r], 1)
            curr_or = bits_to_int(bits)

            while curr_or >= k and left_p <= r: 
                res = min(res, r - left_p + 1)
                bits_update(bits, nums[left_p], -1)  
                curr_or = bits_to_int(bits)
                left_p += 1

        return -1 if res == float("inf") else res
