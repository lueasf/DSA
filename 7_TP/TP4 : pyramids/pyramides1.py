# Pyramides

# Ex1
def lineIndex(line: int, column: int):
    n = 0
    for i in range(1,line):
        n += i 
    return n + column -1

# Ex2
# Q1 O(n!)
def permutations(n):
    L = [i for i in range(1,n+1)]
    res = []
    sol = [] # partial sol

    def dfs():
        if len(sol) == n:
            res.append(sol[:])
            return
        for x in L:
            if x not in sol:
                sol.append(x)
                dfs()
                sol.pop()
    dfs()
    return res
        

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

# Q3 O(h²×n!)
def solve(h):
    res = []
    n = (h*(h+1))//2
    for perm in permutations2(n):
        if correct(perm, h):
            res.append(perm)
    return res

import time
def test_performance_quick(h, iterations=100):
    total_time = 0
    results = []

    for _ in range(iterations):
        start_time = time.time()
        result = solve(h)
        end_time = time.time()
        
        execution_time = end_time - start_time
        total_time += execution_time
        results.append(len(result))

    average_time = total_time / iterations
    average_solutions = sum(results) / iterations

    print(f"Test pour validPermutations({h}):")
    print(f"Nombre d'itérations: {iterations}")
    print(f"Temps moyen d'exécution: {average_time:.6f} secondes")
    print(f"Nombre moyen de solutions: {average_solutions:.2f}")
    print(f"Temps total pour {iterations} exécutions: {total_time:.6f} secondes")

test_performance_quick(3)