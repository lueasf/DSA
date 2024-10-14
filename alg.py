"""
#5 étapes pour résoudre un problème

1) simplifier le problème.
A l'oral, il faut savoir expliquer le problème.
Trouver les cas de base et d'exception

2) Trouver le pattern
Structure de données et algorithme
-Trouver une première reponse rapide
-Une solution optimale peut survenir
-Regarder si une complexité de temps est demandé.
Ex : O(log(n)) demande un binary search algo

-si il y a des noeuds/chemins : c'est peut-etre un graphe
-si il y a un sens de direction : c'est peut-être un graphe

3) Mettre le pattern en place
-Mettre l'algorithme trouvé en place
-chercher d'autres conditions.

4) Utiliser la doc si besoin

5) Tester
Regarder ligne par ligne si il y a un problème.

"""

# DFS (Depth-First Search) : Parcours en profondeur
def dfs(node):
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in get_neighbors(node):
            dfs(neighbor)
    return visited


# BFS (Breadth-First Search) : Parcours en largeur
from collections import deque

def get_neighbors(node):
    pass

def bfs(start_node):
    queue = deque([start_node])
    visited = set([start_node])
    
    while queue:
        current_node = queue.popleft()

        for neighbor in get_neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Merge Sort O(n log n) : Tri fusion
# algo de tri par division et fusion
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_sort(left, right) # merge les tableaux

# Quick Sort O(n log n) : Tri rapide
# algo de tri par partition
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Dijkstra



alors= "ondanse"
print(f"Ce fichier est {__file__}")
print(f"ce fichier utilise la fonction {dfs.__name__}")
print(f"ce fichier utilise la variable alors={alors}")