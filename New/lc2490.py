# O(n) temps et espace

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        L = sentence.split()
        if L[-1][-1] != L[0][0]:
            return False
        for i in range(len(L)-1):
            if L[i][-1] != L[i+1][0]:
                return False
        return True
        