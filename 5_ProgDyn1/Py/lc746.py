# Min Cost Climbing Stairs : Google
# On remarque que l'arbre se répète donc on pense à la prog dyn.
# Avec la liste, on peut completer le problème à l'envers.

# BYME
class Solution:
    def minCostClimbingStairs(cost):
        for i in range(3,len(cost)+1):
            cost[-i] = min(cost[-i]+cost[-i+1], cost[-i] + cost[-i+2])
        return min(cost[0],cost[1])