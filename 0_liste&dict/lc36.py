# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:


#BYME
def isValidSudoku(board : list[list[str]]):
        #Lignes
        for i in range(9):
            dico = dict()
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] not in dico:
                        dico[board[i][j]] = 1
                    else:
                        return False

        #Colones
        for i in range(9):
            dico = dict()
            for j in range(9):
                if board[j][i].isdigit():
                    if board[j][i] not in dico:
                        dico[board[j][i]] = 1
                    else:
                        return False
        
        #Carré
        for i in range(3):
            for j in range(3):
                set_ = set()
                for k in range(3):
                    for l in range(3):
                        val = board[i*3+k][j*3+l]
                        if val.isdigit():
                            if val in set_:
                                return False
                            else :
                                set_.add(val)
        
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