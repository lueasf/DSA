# Interview Questions

### 1) C'est quoi le Global Interpreter Lock (GIL) en Python ?
# Le GIL est un mécanisme propre à l'implémentation CPython.
# Il permet d'assurer qu'un seul thread exec du bytecode Python à la fois.

### 2) C'est quoi le scope en Python ?
# Un scope, c’est la portée dans laquelle une variable est définie et accessible. 
# Python utilise une règle appelée LEGB pour chercher une variable :
# Local : dans la fonction actuelle
# Enclosing : dans une fonction englobante
# Global : dans le module actuel
# Built-in : dans les fonctions intégrées de Python

### 3) Quelle est la différence entre global et nonlocal ?
# Le mot clé global permet de modifier une var global depuis une fonction.
# Le mot clé nonlocal permet de modifier une var englobante depuis une fonction imbriquée.

### 4) Que se passe-t-il quand on fait a = b en mémoire ?
# Quand on fait a = b, on ne copie pas l’objet, on crée juste une nouvelle référence vers le même objet.
# a et b pointent vers le même objet en mémoire.
# pour faire une vraie copie, il faut utiliser la fonction copy() ou deepcopy().

### 5) c'est quoi *args et **kwargs ?
# *args permet de passer un nombre variable d'arguments positionnels à une fonction (sans noms).
# **kwargs permet de passer un nombre variable d'arguments nommés à une fonction (avec noms).
# Args les regroupent dans un tuple et kwargs dans un dictionnaire.
def addition(*nombres):
    total = 0
    for n in nombres:
        total += n
    return total

addition(1, 2, 3, 4)  # ➜ 10

### 6) Quelle est la différence entre une liste et un générateur en Python ?
# une liste est evaluée immédiatement et stockée en mémoire.
# un gen est evalué à la demande
[x for x in range(10)]  # liste
(x for x in range(10))  # générateur
# yield fait une pause dans la fonction et renvoie une valeur.

### 7) Méthodes spéciales en Python, permettent de creer de classes personnalisées en OOP
# __init__ : constructeur de la classe
# __str__ : pour afficher la classe sous forme de chaîne de caractères (print)
# __len__ : pour obtenir la longueur d'un objet (len)

### 8) C'est quoi __main__ en python ?
# __main__ est le nom du module principal qui est exécuté.
# dans notre fichier, __name__ est egal au nom du fichier si il est importé sans .py.

### 9) Les threads en Python ?
# Un thread est une unité d'exécution au sein d’un programme.

### 10) Les decorators en Python ?
# Un decorator est une fonction qui modifie le comportement d'une autre fonction.
# Décorateur
def mon_decorateur(fonction):
    def fonction_modifiee():
        print("Avant d'exécuter la fonction")
        fonction()  # Appel de la fonction d'origine
        print("Après avoir exécuté la fonction")
    return fonction_modifiee

# Fonction à décorer
@mon_decorateur  # Application du décorateur
def dire_bonjour():
    print("Bonjour!")

# Appel de la fonction décorée
dire_bonjour()

# Ici, @mon_decorateur est un raccourci pour : dire_bonjour = mon_decorateur(dire_bonjour)
# Ex, en flask : @app.route('/home')

### 11) C'est quoi un context manager ?
# Un context manager en Python est un objet qui définit comment gérer une ressource 
# pendant une période donnée. Cela est particulièrement utile pour gérer des ressources 
# comme des fichiers, des connexions réseau ou des verrous (locks). Ex : open()

### 12) C'est quoi un lambda en Python ?
# Un lambda est une fonction anonyme, c'est-à-dire une fonction sans nom.
# Ex :
addition = lambda x, y: x + y

### Pourquoi Python ? Python est un lang de prog de haut niveau (facile à lire et à écrire).
# interprété (pas compilé), dynamique (pas de déclaration de type), orienté objet (OOP).
# Il est portable (peut s'exécuter sur n'importe quel OS), 

### les langages et leur paradigme/ modèle de programmation
# langage impératif : repose sur l'exec d'instructions séquentielles. (C, C++, Java, Python)
# langage fonctionnel : repose sur des fonctions pures. Empeche les effets de bord. (les fonctions
    # retournent juste des valeurs). (Haskell, Lisp, Elixir)
# lanage OOP : objets avec des attributs et des méthodes. (Java, C++, Python, Ruby, C#)
# langage logique : repose sur des règles logiques. (Prolog, Mercury)
# langage déclaratif : décrit le résultat souhaité sans spécifier comment l'obtenir. (SQL, HTML)
# langage procédural : repose sur des procédures ou des fonctions. (C, Pascal, Fortran)



## Algorithmes 

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

# Calcul rapide de (x^y) % mod avec exponentiation rapide
def power_mod(x, y, mod):
    res = 1
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % mod
        x = (x * x) % mod
        y //= 2
    return res

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


alors= "ondanse"
print(f"Ce fichier est {__file__}")
print(f"ce fichier utilise la fonction {dfs.__name__}")
print(f"ce fichier utilise la variable alors={alors}")
