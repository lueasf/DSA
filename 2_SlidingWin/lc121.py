# Best time to buy and sell stock : Google

# Buy low and sell high

# BYME
class Solution:
    def maxProfit(self, prices) -> int:
        l, r = 0,1
        curr_max = 0
        while r<len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                m = prices[r] - prices[l]
                if curr_max < m:
                    curr_max = m
            r += 1
        return curr_max