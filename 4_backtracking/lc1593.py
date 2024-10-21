class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen):
            if(start==len(s)):
                return 0
            max_sp = 0

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in seen:
                    seen.add(substring)
                    max_sp = max(max_sp, 1 + backtrack(end, seen)) 
                    seen.remove(substring)
            return max_sp
        
        return backtrack(0, set())