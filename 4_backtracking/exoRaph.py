## ob : orange ,p = 2 ; banane , p=3; artichaud ,p =5 ; 
# sac de taille 10
# renvoyer le sac a dos le plus complet possible
from copy import deepcopy

truc = [2,3,5]
taillesac = 10
sac = []

def sacc(obj,sac, taillesac):
    sac = deepcopy(sac)
    cap = taillesac - sum(sac)
    sacs = []
    for i in range(len(obj)):
        if cap > 0:
            sac.append(obj[i]) 
            nouveausacc = sacc(obj, sac, taillesac)
            sacs.append(nouveausacc)
        if (cap == 0):
            sacs.append(sac)
        else :
            if sac != []:
                sac.pop()
                sacs.append(sac)
    vraisac = 0
    for i in sacs:
        s = sum(i)
        if s >= vraisac:
            vraisac = s
            val = i
    return val

#si on met un paramètre dans la fonction et qu'on le change par la suite, ça fait une erreur.

# OU

def backtracking(sac, objets, taille):
    if taille == 0:
        return sac
    if len(objets) == 0:
        return sac
    if taille < 0:
        return sac
    else:
        sac.append(objets[0])
        sac1 = backtracking(sac, objets[1:], taille - objets[0])
        sac.pop()
        sac2 = backtracking(sac, objets[1:], taille)
        if len(sac1) > len(sac2):
            return sac1
        else:
            return sac2

a = []
def f(b): # car le paramètre b est un pointeur 
    b.append(1) # donc en appelant la fonction f(a), on modifie a
    return b 
# on peut faire : L = L[:]

if '__main__' == __name__:
    print(sacc([2,3,5,9,7],[],15))
    print(a)
    print(f(a))
    print(a)
    pass