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

a = []
def f(b):
    b.append(1)
    return b


if '__main__' == __name__:
    print(sacc([2,3,5,9,7],[],15))
    print(a)
    print(f(a))
    print(a)
    pass