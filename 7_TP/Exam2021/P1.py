def indice_de_position(position: tuple[int, int], taille_cote: int) -> int:
    return ((position[0]-1) * taille_cote) + position[1] - 1


def suivants(position: tuple[int, int], taille_cote: int) -> list[tuple[int, int]]:
    pos = [(2,1),(2,-1),(1,2),(-1,2),(-2,-1),(-2,1),(1,-2),(-1,-2)]
    L = []
    li, col = position
    for x,y in pos:
        if (col + x <= taille_cote and col + x >= 1 and li + y <= taille_cote and li + y >= 1):
            L.append((col+x,li+y))
    return L

def cavalier(echiquier: list[int], position: tuple[int, int], taille_cote: int) -> bool:
    
    def dfs(echiquier, position):
        if all(num==1 for num in echiquier):
            return True

        ind = indice_de_position(position, taille_cote) # cadrillage into liste
        
        res_tup = suivants(position, taille_cote)
        for (x,y) in res_tup:
            pos_xy_liste = indice_de_position((x,y),taille_cote)

            if echiquier[pos_xy_liste] == 0:
                echiquier[pos_xy_liste] = 1
                if dfs(echiquier,(x,y)):
                    return True
            else:
                continue
            echiquier[pos_xy_liste] = 0
        
        return False
    return dfs(echiquier,position)

taille = 5
ech = [ 0 for i in range(taille*taille)]
ech[indice_de_position((3,3),taille)] = 1
pos = (3,3)
print(cavalier(ech, pos, taille))


def chemin_cavalier(echiquier: list[int], position: tuple[int, int], taille_cote: int) -> tuple[bool, list[tuple[int, int]]]:
    L = [position]
    def dfs(echiquier, position,L):
        if all(num==1 for num in echiquier):
            return True, L

        ind = indice_de_position(position, taille_cote) # cadrillage into liste
        
        res_tup = suivants(position, taille_cote)
        for (x,y) in res_tup:
            pos_xy_liste = indice_de_position((x,y),taille_cote)

            if echiquier[pos_xy_liste] == 0:
                echiquier[pos_xy_liste] = 1
                L.append((x,y))
                if dfs(echiquier,(x,y),L):
                    return True
            else:
                continue
            echiquier[pos_xy_liste] = 0
            L.pop()
        
        return False, []
    return dfs(echiquier,position,L)


if __name__ == "__main__":
    pass