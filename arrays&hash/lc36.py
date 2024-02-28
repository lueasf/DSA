# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# MARCHE PAS.

def isValidSudoku(board : list[list[str]]):
    set_largeur = set()
    for i in range(9):
        for j in range(9):
            if board[i][j].isdigit and board[i][j] in set_largeur:
                return False
            else:
                set_largeur.add(int(board[i][j]))

    set_longeur = set()
    for i in range(0):
        if board[i][0].isdigit and board[i][0] in set_longeur:
            return False
        else:
            set_longeur.add(int(board[i][0]))
    
    # regarder si il y a des doublons dans les carrés
    set_carre = set()
    for i in range(3):
        for j in range(3):
            if board[i][j].isdigit and board[i][j] in set_carre:
                return False
            else:
                set_carre.add(int(board[i][j]))
    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))