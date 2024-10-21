n = 4
echiquier = [0 for _ in range(n*n)]


def indice_de_position(position: tuple[int, int], taille_cote: int) -> int:
    return (position[0] - 1) * taille_cote + (position[1] - 1)


def suivants(position: tuple[int, int], taille_cote: int) -> list[tuple[int, int]]:
    
    possibles = []

    # Déplacements possibles théoriquement a partir d'une case (ligne, colonne)
    deplacements = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]

    for dx, dy in deplacements:

        nouvelle_position = (position[0] + dx, position[1] + dy)

        # Si la nouvelle position est bien sur l'échiquier, on l'ajoute a la liste
        if 1 <= nouvelle_position[0] <= taille_cote and 1 <= nouvelle_position[1] <= taille_cote:
            possibles.append(nouvelle_position)

    return possibles

# Renvoie True si toutes les cases de l'échiquier ont été vérifiées
def tout_visite(echiquier: list[int]) -> bool:
    for c in echiquier:
        if c != 1:
            return False
    return True


def cavalier(echiquier: list[int], position: tuple[int, int], taille_cote: int) -> bool:
    
    # Met a jour la case du cavalier
    echiquier[indice_de_position(position, taille_cote)] = 1

    if tout_visite(echiquier):
        return True

    # On récupère toutes les positions suivantes possibles et on les essaie
    for pos in suivants(position, taille_cote):

        # Si la case a déjà été visitée, on passe au déplacement suivant
        if echiquier[indice_de_position(pos, taille_cote)] == 1:
            continue

        # On essaie le déplacement
        # On fait bien une copie de l'échiquier car il va être modifié après
        # Une autre solution est de le re-modifier pour annuler les changements qu'on a fait, cf cavalier2
        resultat = cavalier(echiquier[:], pos, taille_cote)

        # On a réussi a parcourir toutes les cases en faisant ce déplacement, on renvoie True
        if resultat:
            return True

    # On a testé tous les déplacements et aucun n'a marché, on renvoie False
    return False


# Même chose que la fonction précédente mais on évite de faire une copie en annulant les modifications qu'on fait à l'échiquier
# on a donc une complexité en espace plus faible, mais on a une complexité en temps plus élevée
def cavalier2(echiquier: list[int], position: tuple[int, int], taille_cote: int) -> bool:
    
    # Met a jour la case du cavalier
    echiquier[indice_de_position(position, taille_cote)] = 1

    if tout_visite(echiquier):
        return True

    # On récupère toutes les positions suivantes possibles et on les essaie
    for pos in suivants(position, taille_cote):

        # Si la case a déjà été visitée, on passe au déplacement suivant
        if echiquier[indice_de_position(pos, taille_cote)] == 1:
            continue

        # On essaie le déplacement
        resultat = cavalier2(echiquier, pos, taille_cote)

        # On a réussi a parcourir toutes les cases en faisant ce déplacement, on renvoie True
        if resultat:
            return True


    # On a testé tous les déplacements et aucun n'a marché, on annule notre déplacement et on renvoie False
    echiquier[indice_de_position(position, taille_cote)] = 1
    return False


# Copié collé de la fonction précédente mais on renvoie les déplacements qu'on a fait
def chemin_cavalier(echiquier: list[int], position: tuple[int, int], taille_cote: int) -> tuple[bool, list[tuple[int, int]]]:
  
    # Met a jour la case du cavalier
    echiquier[indice_de_position(position, taille_cote)] = 1

    if tout_visite(echiquier):
        # On a effectué aucun autre déplacement depuis cette position et on a terminé
        return True, [position]

    # On récupère toutes les positions suivantes possibles et on les essaie
    for pos in suivants(position, taille_cote):

        # Si la case a déjà été visitée, on passe au déplacement suivant
        if echiquier[indice_de_position(pos, taille_cote)] == 1:
            continue

        # On essaie le déplacement
        # On fait bien une copie de l'échiquier car il va être modifié après
        # Une autre solution est de le re-modifier pour annuler les changements qu'on a fait, cf fonction suivante
        resultat, deplacements = chemin_cavalier(echiquier[:], pos, taille_cote)

        # On a réussi a parcourir toutes les cases en faisant ce déplacement,
        # on renvoie True et on ajoute la position ou on est a la liste des positions prises
        if resultat:
            return True, [position] + deplacements

    # On a testé tous les déplacements et aucun n'a marché, on renvoie False
    return False, []


# Idem mais en évitant la copie de l'échiquier
def chemin_cavalier2(echiquier: list[int], position: tuple[int, int], taille_cote: int) -> tuple[bool, list[tuple[int, int]]]:
  
    # Met a jour la case du cavalier
    echiquier[indice_de_position(position, taille_cote)] = 1

    if tout_visite(echiquier):
        # On a effectué aucun autre déplacement depuis cette position et on a terminé
        return True, [position]

    # On récupère toutes les positions suivantes possibles et on les essaie
    for pos in suivants(position, taille_cote):

        # Si la case a déjà été visitée, on passe au déplacement suivant
        if echiquier[indice_de_position(pos, taille_cote)] == 1:
            continue

        # On essaie le déplacement
        # On fait bien une copie de l'échiquier car il va être modifié après
        # Une autre solution est de le re-modifier pour annuler les changements qu'on a fait, cf fonction suivante
        resultat, deplacements = chemin_cavalier2(echiquier, pos, taille_cote)

        # On a réussi a parcourir toutes les cases en faisant ce déplacement,
        # on renvoie True et on ajoute la position ou on est a la liste des positions prises
        if resultat:
            return True, [position] + deplacements

    # On a testé tous les déplacements et aucun n'a marché, on annule le déplacement et on renvoie False
    echiquier[indice_de_position(position, taille_cote)] = 0
    return False, []