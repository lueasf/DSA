# Count the Hidden Sequences (Medium)

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
       diff, lowest, highest = 0, 0, 0

        for d in differences:
            diff += d
            lowest = min(lowest, diff)
            highest = max(highest, diff)
            if highest - lowest > upper - lower :
                return 0
        return (upper - lower) - (highest - lowest) + 1

'''
Exemple : differences = [1, -2, 3], lower = 1, upper = 10

On cherche hidden = [x, ?, ?, ?] où :
hidden[1] = x + 1, hidden[2] = (x + 1) - 2 = x - 1, hidden[3] = (x - 1) + 3 = x + 2

Tous ces nombres doivent être ≥ 1 et ≤ 10.
Étapes :
1) Calculer les écarts (diff) par rapport à x (simule hidden[i] - x) :
Après [1] → diff = +1, Après [-2] → diff = -1, Après [3] → diff = 2
    → Écart min (lowest) = -1 (vient de x - 1)
    → Écart max (highest) = 2 (vient de x + 2)

2) Contraintes sur x :
Le plus petit nombre dans la séquence est x + lowest = x - 1 → doit être ≥ lower
  → x - 1 ≥ 1 → x ≥ 2
Le plus grand nombre est x + highest = x + 2 → doit être ≤ upper
  → x + 2 ≤ 10 → x ≤ 8

3) Combien de x satisfont ça ?
x peut être 2, 3, 4, 5, 6, 7, 8 → 7 valeurs possibles.
'''
