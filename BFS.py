# Parcours en largeur
# EXEMPLE : résoudre un sudoku

def solve_sudoku(board):
    q = [board]
    DejaVu = [board]
    while q != []:
        temp = q.pop(0)
        if is_complete(temp):
            return temp
        else:
            for neighbor in generate_neighbors(temp):
                if neighbor not in DejaVu:
                    DejaVu.append(neighbor)
                    q.append(neighbor)
    return None

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Return row, col
    return None

def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True

def generate_neighbors(board):
    empty_cell = find_empty(board)
    if not empty_cell:
        return []
    row, col = empty_cell 
    n = []
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            new_board = [row[:] for row in board]
            new_board[row][col] = num
            n.append(new_board)
    return n

def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def display(board):
    for row in board:
        print(" ".join(map(str, row)))


# Example usage:
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Initial Sudoku Board:")
display(board)

solution = solve_sudoku(board)
if solution:
    print("\nSudoku Solved:")
    display(solution)
else:
    print("\nNo solution exists.")