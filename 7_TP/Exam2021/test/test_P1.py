from util import *
import sys
sys.path.append("..")
sys.path.append(".")

import P1

print_test_start()

#
#   Test indice_de_position
#

with TestCase("indice_de_position - première case") as t:
    i = P1.indice_de_position((1,1), 42)
    if i != 0:
        t.fail(f"L'indice de la case (1,1) devrait être 0 et non {i}")

with TestCase("indice_de_position - dernière case") as t:
    i = P1.indice_de_position((10,10), 10)
    if i != 99:
        t.fail(f"L'indice de la case (10,10) devrait être 99 et non {i}")

with TestCase("indice_de_position - case en 2ème ligne") as t:
    i = P1.indice_de_position((2,1), 5)
    if i != 5:
        t.fail(f"L'indice de la case (2,1) devrait être 5 et non {i} (attention à l'ordre des lignes et des colonnes dans la position)")

#
#   Tests suivants
#

with TestCase("suivants - case dans un coin") as t:
    positions = set(P1.suivants((1,1), 5))
    positions_possibles = {(2,3), (3,2)}
    if positions != positions_possibles:
        t.fail(f"Positions attendues : {positions_possibles}\nPositions renvoyées : {positions}\nPositions manquantes : {positions_possibles - positions}\nPositions en trop : {positions - positions_possibles}")

with TestCase("suivants - case sur un bord") as t:
    positions = set(P1.suivants((3,1), 5))
    positions_possibles = {(1,2), (2,3), (4,3), (5,2)}
    if positions != positions_possibles:
        t.fail(f"Positions attendues : {positions_possibles}\nPositions renvoyées : {positions}\nPositions manquantes : {positions_possibles - positions}\nPositions en trop : {positions - positions_possibles}")

with TestCase("suivants - case au milieu") as t:
    positions = set(P1.suivants((3,3), 5))
    positions_possibles = {(1,2), (2,1), (1,4), (2,5), (4,1), (5,2), (4,5), (5,4)}
    if positions != positions_possibles:
        t.fail(f"Positions attendues : {positions_possibles}\nPositions renvoyées : {positions}\nPositions manquantes : {positions_possibles - positions}\nPositions en trop : {positions - positions_possibles}")


#
#   Test cavalier
#

with TestCase("cavalier - Echiquier de taille 4", "Aucune solution n'existe pour un échiquier de taille 4") as t:
    
    n = 4
    echiquier = [0 for _ in range(n*n)]

    resultat = P1.cavalier(echiquier, (1,1), n)

    if resultat != False:
        t.fail("La fonction n'a pas renvoyé False")


with TestCase("cavalier - Echiquier de taille 5", "Il y a des solutions pour un échiquier de taille 5") as t:
    
    n = 5
    echiquier = [0 for _ in range(n*n)]

    resultat = P1.cavalier(echiquier, (1,1), n)

    if resultat != True:
        t.fail("La fonction n'a pas renvoyé True")

desc = "Vérifie que la fonction prend bien en compte les cases déjà visitées sur l'échiquier.\nIci toutes les cases sauf celle sur laquelle se trouve le cavalier ont été visitées, il n'y a rien a faire"
with TestCase("cavalier - Echiquier déjà rempli", desc) as t:
    
    n = 4
    echiquier = [1 for _ in range(n*n)]

    echiquier[0] = 0

    resultat = P1.cavalier(echiquier, (1,1), n)
    
    if resultat != True:
        t.fail("La fonction doit renvoyer True si toutes les cases ont déjà été visitées")


#
#   Test chemin_cavalier
#

with TestCase("chemin_cavalier - Echiquier de taille 4", "Aucune solution n'existe pour un échiquier de taille 4") as t:
    
    n = 4
    echiquier = [0 for _ in range(n*n)]

    resultat, _ = P1.chemin_cavalier(echiquier, (1,1), n)

    if resultat != False:
        t.fail("La fonction n'a pas renvoyé False")


with TestCase("chemin_cavalier - Echiquier de taille 5", "Il y a des solutions pour un échiquier de taille 5") as t:
    
    n = 5
    echiquier = [0 for _ in range(n*n)]

    resultat, _ = P1.chemin_cavalier(echiquier, (1,1), n)

    if resultat != True:
        t.fail("La fonction n'a pas renvoyé True")

desc = "Vérifie que la fonction prend bien en compte les cases déjà visitées sur l'échiquier.\nIci toutes les cases sauf celle sur laquelle se trouve le cavalier ont été visitées, il n'y a rien a faire"
with TestCase("chemin_cavalier - Echiquier déjà rempli", desc) as t:
    
    n = 4
    echiquier = [1 for _ in range(n*n)]

    echiquier[0] = 0

    resultat, chemin = P1.chemin_cavalier(echiquier, (1,1), n)
    
    if resultat != True:
        t.fail("La fonction doit renvoyer True si toutes les cases ont déjà été visitées")

    if chemin != [(1,1)]:
        t.fail("Le chemin emprunté par le cavalier doit contenir la case où il se trouve initialement, le chemin ne doit être vide que lorsqu'il n'y a pas de solution")


with TestCase("chemin_cavalier - chemin", desc) as t:
    
    # L'échiquier ressemble a ça, 1 seul chemin possible (numéroté)
    #      1   2   3   4    
    #    +---+---+---+---+
    #  1 | 0 | x | x | x |
    #    +---+---+---+---+
    #  2 | x | x | 1 | 4 |
    #    +---+---+---+---+
    #  3 | 2 | x | x | x |
    #    +---+---+---+---+
    #  4 | x | x | 3 | x |
    #    +---+---+---+---+
    #

    n = 4
    echiquier = [0,1,1,1,1,1,0,0,0,1,1,1,1,1,0,1]

    resultat, chemin = P1.chemin_cavalier(echiquier, (1,1), n)
    
    if resultat != True:
        t.fail("La fonction doit renvoyer True car un chemin existe")

    chemin_attendu = [(1,1), (2,3), (3,1), (4,3), (2,4)]

    if chemin != chemin_attendu:
        t.fail(f"Chemin attendu : {chemin_attendu}\nChemin obtenu  : {chemin}")



tests_summary()
