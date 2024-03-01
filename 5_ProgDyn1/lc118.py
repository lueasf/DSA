# renvoyer la liste du triangle de pascal 
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
            
        output = []
        for i in range(numRows):
            output.append([1]*(i+1))
        
        for j in range(2, numRows):
            for k in range(1, j):
                output[j][k] = output[j-1][k-1] + output[j-1][k]

        return output
    

# PROG DYNAMIQUE
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]

        for i in range(1, numRows):
            row = [1] * (i + 1)

            for j in range(1, len(row) - 1):
                row[j] = ans[i - 1][j - 1] + ans[i - 1][j]

            ans.append(row)

        return ans