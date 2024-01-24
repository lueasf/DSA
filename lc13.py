# roman to integer

class Solution:
    def romanToInt(self, s: str) -> int:
        dico = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for j in range(len(s)):
            if (j<len(s)) and (dico[s[j]] < dico[s[j+1]]):
                res -= dico[s[j]]
            else :
                res += dico[s[j]]
        return res + dico[s[-1]]
    
