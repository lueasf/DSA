# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = []
        for i in range(len(s)):
            l = []
            for j in range(i, len(s)):
                if not s[j] in l:
                    l.append(s[j])
                else:
                    break
            res.append(l)
        
        if len(res) == 1:
            return len(res[0])
        return len(max(res, key = len))
    
# dans res, on ajoute plein de sous-chaine sans répétition en on renvoie la plus longue
    