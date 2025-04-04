# Longest Palindromic Substring : Google


# BY LC
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # immpair
            l,r = i,i
            while l >= 0 and r< len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = len(res) # r - l + 1
                l -= 1
                r += 1
            
            # pair
            l,r = i, i +1
            while l>= 0 and r< len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1

        return res
