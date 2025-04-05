# Number of 1 bits : Hamming Weigh : Amazon

# on veut savoir combien de bits sont a 1 dans ce nombre

# FAV

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n: # (!= 0)
            res += n & 1   # ope bit a bit de l'unité
            n >>= 1 # on décale
        return res