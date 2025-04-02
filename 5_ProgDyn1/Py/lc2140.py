
from typing import List


# BYME
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dico = [0] * (n+1)

        for i in range(n - 1, -1, -1):
            points, bp = questions[i]
            next = 1 + i + bp
            dico[i] = max(points + (dico[next] if next < n else 0), dico[i + 1])
                
        return max(dico)