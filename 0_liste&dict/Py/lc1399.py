# Count Largest Group (1399 - Easy)

class Solution:
    def countLargestGroup(self, n: int) -> int:
        dico = {}

        for i in range(1, n + 1):
            key = sum(int(x) for x in str(i))
            if key not in dico:
                dico[key] = 0
            dico[key] +=1

        maxval = max(dico.values())
        count = sum(1 for v in dico.values() if v == maxval)

        return count
