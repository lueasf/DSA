# 498. Diagonal Traverse
# i + j constant for each col, if even go right, else bottom

from pyparsing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        res = []
        row = col = 0

        for _ in range(m * n):
            res.append(matrix[row][col])

            if (col + row) % 2 == 0:
                if col == n - 1:
                    row += 1 # right
                elif row == 0:
                    col += 1 # bottom
                else:
                    row -= 1
                    col += 1
            
            else:
                if row == m - 1:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return res
        