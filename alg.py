# DFS (Depth-First Search) 
def dfs(node):
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in get_neighbors(node):
            dfs(neighbor)
    return visited


# BFS (Breadth-First Search)
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

# Dijkstra

"""
# 5 étapes pour résoudre un problème
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

alors= "ondanse"
print(f"Ce fichier est {__file__}")
print(f"ce fichier utilise la fonction {dfs.__name__}")
print(f"ce fichier utilise la variable alors={alors}")