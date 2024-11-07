from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int: 
        max_bit_position = max(candidates).bit_length()
        bit_count = [0] * max_bit_position # en bc[0] c'est à si le bit est a 0, 1 sinon de tout les candidates
 
        for num in candidates:
            for i in range(max_bit_position):
                if (num >> i) & 1: 
                    bit_count[i] += 1

        # La plus grande combinaison correspond au maximum des bits à 1.
        return max(bit_count)

# candidates = [16, 17, 71, 62, 12, 24, 14]
# avec ce candidats, bit_count = [2, 3, 1, 4, ...] :
# Position 0 (bit le plus à droite) : Le bit est activé (1) dans 2 nombres parmi candidates.
# Position 1 : Le bit est activé dans 3 nombres.
