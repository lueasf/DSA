# Palindromic substring

# Meme que pour leetcode 5 mais cette fois on verifie pas que c'est le plus long


# BYME
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # immpair
            l,r = i,i
            while l >= 0 and r< len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # pair
            l,r = i, i +1
            while l>= 0 and r< len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res
        