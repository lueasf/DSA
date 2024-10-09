# Climbing stairs

# il s'agit d'un arbre de décision avec 2 choix à chaque fois: ajouter 1 ou 2.
# O(2^n) si on fait avec DFS
# or on remarque que l'arbre compute plusieurs fois le même problème.
# on obtient alors O(n) grace à la mémoisation
# on remarque que tout dépend du cas de base, donc on va commencer par ça.
# C'est du DP-Bottom Up
# On va utiliser un tableau
# etage 0, 1, 2, 3, 4, 5
#       8, 5, 3, 2, 1, 1 (avec 1, 1 = one, two)

def climbStairs(n):
    one, two = 1, 1

    for i in range(n -1):
        temp = one
        one = one + two
        two = temp
    return one
        
        