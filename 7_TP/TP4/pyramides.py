# Pyramides

# Ex1
def lineIndex(line: int, column: int):
    n = 0
    for i in range(1,line):
        n += i 
    return n + column -1

# Ex2
# Q1
def permutations(n):
    L = [i for i in range(n)]
    res = []
    def dfs(index):
        if index == n:
            res.append(L.copy())
            return
        else:
            for i in range(n):
                L[index], L[i] = L[i], L[index]
                dfs(index+1)

                L[index], L[i] = L[i], L[index]
        return res
    return dfs(0)

def permutations2(n):
    from itertools import permutations as it_permutations
    L = list(range(1, n + 1))
    return list(it_permutations(L))


# Q2
def correct(pyramide, h):
    n = (h*(h+1))//2
    if sorted(pyramide) != list(range(1, n+1)):
        return False

    for line in range(h-1, -1, -1): # va de h-1 compris a 0 compris
        for col in range(1, line +1):

            curr = pyramide[lineIndex(line, col)]
            left = pyramide[lineIndex(line+1, col)]
            right = pyramide[lineIndex(line+1, col+1)]

            if curr != abs(left - right):
                return False

    return True

# Q3
def solve(h):
    res = []
    n = (h*(h+1))//2
    for perm in permutations2(n):
        if correct(perm, h):
            res.append(perm)
    return res

print(solve(3))