# word search

# bruteforce solution = backtracking
# DFS : Depth-First Search 

class Solution:
    def exist(self, board, word):
        r, c = len(board), len(board[0])
        path = set()

        def dfs(ro, co, i):
            if i == len(word):
                return True
            if ():
                pass
