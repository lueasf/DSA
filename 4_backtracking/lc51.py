# Le problème des N reines

# On utilise un quadrillage avec :
# __
# |     l'axe des x et y. On va garder en mémoire les coordonées des diagonales positives et négatives
# de la ou on a mis les reines. Pas besoin de garder les lignes car on sait qu'on doit avancer l'index 
# à chaque itération.

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

#  BYME 
def solveNQueens(n):
    col = set()
    posDiag = set() # r + c (row + col)
    negDiag = set() # r - c       

    res = []
    board = [["."]*n for i in range(n)] 
    def backtrack(r):
        if r == n :
            copy = ["".join(r) for r in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            #cleanup 
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

        
        return res
    return backtrack(0)

print(solveNQueens(1))