# BYME

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = dict()
        n = len(s)
        for i in range(n):
            d[s[i]]= i

        l = 0
        r = 0
        res = []
        
        for i in range(n):
            r = max(r, d[s[i]])
            if i == r:
                res.append(r - l + 1)
                l = i + 1

        return res
    
print(Solution().partitionLabels("ababcbacadefegdehijhklij"))