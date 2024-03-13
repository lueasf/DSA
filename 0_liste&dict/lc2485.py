# exercice de pivor

# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

def pivotInteger(n):
    petit = []
    grand = [i for i in range(1,n+1)]
    for i in range(1, n):
        petit.append(i)
        if sum(petit) == sum(grand):
            return len(petit)
        grand = grand[1:]
    return -1

print(pivotInteger(8))