# Counting bits

class Solution:
    def countBits(n):
        dp = [0] * (n+1)
        offset = 1 
        for i in range(1,n+1):
            if 2*offset == i:
                offset*=2
            dp[i] = 1 + dp[i - offset]
        return dp
