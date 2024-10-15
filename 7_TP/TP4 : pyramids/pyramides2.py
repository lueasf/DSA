# Pyramides
import time

# Ex1
def lineIndex(line: int, column: int):
    n = 0
    for i in range(1, line):
        n += i
    return n + (column - 1)

def correctBis(pyramide, h, rank):
    n = (h*(h+1)) // 2
    for line in range(h-1, 0, -1): # va de h-1 compris a 0 non compris
        for col in range(1, line +1):
            index_curr = lineIndex(line, col)
            if index_curr >= rank:
                return True

            index_left = lineIndex(line+1, col)
            index_right = lineIndex(line+1, col+1) 
            
            if index_left >= rank or index_right >= rank:
                continue 

            curr = pyramide[index_curr]
            left = pyramide[index_left]
            right = pyramide[index_right]

            if curr != abs(left - right):
                return False

    return True

def validPermutations(n, h):
    res = []
    L = list(range(1, n + 1))
    used = [False]*n # éléments déjà utilisés
    curr = [] # tempo

    def dfs(rank):
        if len(curr) == n:
            res.append(curr.copy())
            return
        
        for i in range(n):
            if not used[i]:
                used[i] = True

                curr.append(L[i])
                if correctBis(curr, h, len(curr)):
                    dfs(rank + 1)

                curr.pop()
                used[i] = False

        return res
    return dfs(0)

"""Lorsque tu es dans le premier appel récursif, la boucle for parcourt les indices 
de i = 0, 1, 2, 3, etc., et à chaque itération, dfs() est appelé pour continuer l'exploration.
Chaque nouvel appel relance la boucle for, qui commence à nouveau à i = 0, 1, 2, etc. Si 
un élément comme i = 2 ne fonctionne pas à ce moment-là (car ce n'est pas encore sa place),
tu l'enlèves avec pop(), puis continues avec i = 3. Si cela fonctionne, l'appel récursif 
suivant reviendra sur i = 2, qui est à False dans used, et cette fois, cela peut marcher."""

def test_performance_quick(n, h, iterations=100):
    total_time = 0
    results = []

    for _ in range(iterations):
        start_time = time.time()
        result = validPermutations(n, h)
        end_time = time.time()
        
        execution_time = end_time - start_time
        total_time += execution_time
        results.append(len(result))

    average_time = total_time / iterations
    average_solutions = sum(results) / iterations

    print(f"Test pour validPermutations({n}, {h}):")
    print(f"Nombre d'itérations: {iterations}")
    print(f"Temps moyen d'exécution: {average_time:.6f} secondes")
    print(f"Nombre moyen de solutions: {average_solutions:.2f}")
    print(f"Temps total pour {iterations} exécutions: {total_time:.6f} secondes")

test_performance_quick(6,3)