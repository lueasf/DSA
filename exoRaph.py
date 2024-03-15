L = [1,6,5,4,7,9]
# on veut renvoyer [1,0,0,0,1] si on prends les nombres associées aux index 1.

# si je fais une fonction rec qui appelle une liste qui est en paramètre, alros je dois utiliser deepcopy pcq le paramètre est un pointeur.
# toujours renvoyer des solutions homogène, sinon en recursif ca peut poser pb.
# exemple c.f Rapahel

from copy import deepcopy

def exo(L,S):
    res = [0 for i in range(len(L))]
    return(backtracking(L,S,res,0))

def backtracking(L,S,res_entree,cursor):
    res = deepcopy(res_entree)
    if cursor == len(L):
        return res
    res[cursor] = 1 
    res1, res0 = [], []
    if multiplication_liste(res,L) <= S:
        res1 = backtracking(L,S,res,cursor+1)
    res[cursor] = 0 
    if multiplication_liste(res,L) <= S:
        res0 = backtracking(L,S,res,cursor+1)
    if multiplication_liste(res1,L) == S :
        return(res1)
    elif multiplication_liste(res0,L) == S :
        return(res0)
    else :
        return []
    
def multiplication_liste(L1,L2):
    if (L1 == []) or (L2 == []):
        return 0
    else :
        sum = 0
        for i in range(len(L1)):
            sum += L1[i]*L2[i]
        return sum

if __name__=="__main__" :
    print(exo([1,6,5,4,7,9,3,45,32,12,23],44))
    pass