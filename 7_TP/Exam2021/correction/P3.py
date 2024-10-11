

# Renvoie la liste ds chiffres suivants accessibles a partir d'un chiffre
def chiffres_suivants(chiffres_utilises: list[int], chiffre_actuel: int) -> list[int]:
    
    # Pour chaque chiffre, on a des voisins "directs" (les chiffres qu'on peut
    # atteindre sans passer par d'autres chiffres) et des voisins "indirects"
    # (les chiffres qu'on peut atteindre en passant par un autre chiffre)
    # On stocke ça dans une liste de tuples de voisins tel que
    # voisins[i] = (liste_voisins_directs, liste_voisins_indirects)
    # ou chaque voisin indirect est un tuple : (chiffre_par_lequel_on_passe, chiffre_atteint)
    #
    # Tous les chiffres sont décalés de 1 car les listes sont indexées a partir de 0

    voisins = [
        ([2,4,6,8,5], [(2,3), (4,7), (5,9)]), # 1
        ([1,4,7,5,3,6,9], [(5,8)]),         # 2
        ([2,4,6,8,5], [(2,1), (6,9), (5,7)]), # 3
        ([1,2,3,5,7,8,9], [(5,6)]),         # 4
        ([1,2,3,4,6,7,8,9], []),            # 5
        ([1,2,3,5,7,8,9], [(5,4)]),         # 6
        ([2,4,6,8,5], [(4,1), (8,9), (5,3)]), # 7
        ([1,4,7,5,3,6,9], [(5,2)]),         # 8
        ([2,4,6,8,5], [(8,7), (6,3), (5,1)]), # 9
    ]

    possibles = []

    # On commence par ajouter les voisins directs qu'on a pas encore utilisé
    for chiffre in voisins[chiffre_actuel - 1][0]:
        if chiffre not in chiffres_utilises:
            possibles.append(chiffre)

    # Puis on ajoute les voisins indirects si le chiffre par lequel on passe est utilisé
    for chiffre_passe, chiffre in voisins[chiffre_actuel - 1][1]:
        if chiffre_passe in chiffres_utilises and chiffre not in chiffres_utilises:
            possibles.append(chiffre)

    return possibles


def compute_unlock_patterns_count(max_length: int) -> int:
    
    # On fait une fonction auxiliaire car on a besoin de la liste des chiffres utilisés et du chiffre actuel
    def aux(chiffres_utilises: list[int], chiffre_actuel: int, max_length: int) -> int:

        # Plus aucun chiffre a prendre, on a fini
        if max_length == 0:
            # On a 1 seul pattern, celui ou on reste sur le chiffre de départ
            return 1

        # On peut prendre le pattern avec ce chiffre uniquement ou prendre plus de chiffres
        count = 1

        # On teste tous les chiffres possibles
        for chiffre in chiffres_suivants(chiffres_utilises, chiffre_actuel):
            
            count += aux(chiffres_utilises + [chiffre], chiffre, max_length - 1)

        return count

    # Si jamais le prof essaie de troller
    if max_length == 0:
        return 0

    # On compte le nombre de patterns en partant de chacun des chiffres
    count = 0
    for chiffre in range(1, 10):
        count += aux([chiffre], chiffre, max_length - 1)

    return count


# Même fonction mais on adapte la fonction auxiliaire pour renvoyer les chemins
def compute_unlock_patterns(max_length: int) -> list[str]:
    
    def aux(chiffres_utilises: list[int], chiffre_actuel: int, max_length: int) -> list[str]:

        # Plus aucun chiffre a prendre, on a fini
        if max_length == 0:
            # On a 1 seul pattern, celui ou on reste sur le chiffre de départ
            return f"{chiffre_actuel}"

        # On peut prendre le pattern avec ce chiffre uniquement ou prendre plus de chiffres
        patterns = [f"{chiffre_actuel}"]

        # On teste tous les chiffres possibles
        for chiffre in chiffres_suivants(chiffres_utilises, chiffre_actuel):
            
            patterns_suivants = aux(chiffres_utilises + [chiffre], chiffre, max_length - 1)

            # On ajoute le chiffre actuel au début de chaque pattern suivant avant de l'ajouter
            # a la liste des patterns possibles
            for p in patterns_suivants:
                patterns.append(f"{chiffre_actuel}-{p}")

        return patterns

    # Si jamais le prof essaie de troller
    if max_length == 0:
        return []

    # On compte le nombre de patterns en partant de chacun des chiffres
    patterns = []
    for chiffre in range(1, 10):
        patterns += aux([chiffre], chiffre, max_length - 1)

    return patterns