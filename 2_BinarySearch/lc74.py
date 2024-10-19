# search a 2D matrix : Micorsoft

# BYME

def searchMatrix(matrix, target):
    liste = []
    for i in range(len(matrix)): # i : 0,3
        for j in range(len(matrix[0])): 
            liste.append(matrix[i][j])
    l,r = 0, len(liste)-1
    while (l<=r):
        m = (l + r) // 2
        if liste[m] == target:
            return True
        if liste[m] > target:
            r = m - 1
        else:
            l = m + 1
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))