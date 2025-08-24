# STRUCTURES DE DONNÉES #

"""
Listes dico modifiables, ensembles sans doublons, tuples non modifiables avec ordres.
L = [1,2], D = {1:2}, S = {1,2}, T = (1,2)

Subarray = contiguë : [1,2,3] → [1], [2], [3], [1,2], [2,3], [1,2,3]

Subset = n'importe où : [1,2,3] → [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3], []

Subarray → double boucle for i, for j

Subset → backtracking/DFS"""

# LISTES
L = [1, 2, 3]
L.append(4)
L.insert(0, 0) # Ajoute 0 à l'indice 0

L.pop()
L.pop(0) # Supprime l'élément à l'indice 0 et renvoie la valeur
L.popleft() # Supprime le premier élément de la liste et renvoie la valeur
L.remove(2) # Supprime la valeur 2

L.sort() # Trie la liste
L.reverse() # Inverse la liste
L.index(2) # Renvoie l'indice de la valeur 2
sum(L) # Renvoie la somme des valeurs de la liste
len(L) # Renvoie la taille de la liste
for i,j in enumerate(L): # Renvoie l'indice et la valeur
    print(i, j) # 0 1
#utiliser map:
L = [1, 2, 3]
L2 = list(map(lambda x: x**2, L)) # [1, 4, 9]
#utiliser filter:
L = [1, 2, 3]
L2 = list(filter(lambda x: x%2 == 0, L)) # [2]
#utiliser sorted:
L = [1, 2, 3, 9, 8, 7]
L2 = sorted(L) # [1, 2, 3, 7, 8, 9]
L.count(2) # Renvoie le nombre de fois que la valeur 2 est présente dans la liste
#Sclicing:
L = [1, 2, 3, 4, 5, 6]
L[1:3] # renvoie [2, 3]
L[1:] # renvoie [2, 3, 4, 5, 6]
L[:3] # renvoie [1, 2, 3]
L[::2] # renvoie [1, 3, 5]
L[-1] # renvoie 6
L[-2] # renvoie 5
L[-2:] # renvoie [5, 6]
L[:-2] # renvoie [1, 2, 3, 4]
L[1:-1] # renvoie [2, 3, 4, 5]
L[1:-1:2] # renvoie [2, 4]
L[::-1] # renvoie [6, 5, 4, 3, 2, 1] (inverse la liste)


# break, continue, pass:
for i in range(10):
    if i == 5:
        break # sort de la boucle for, 
    if i == 3:
        continue # passe à l'itération suivante, ici 4
    if i == 2:
        pass # ne fait rien
    print(i)

# TUPLES
t = (1, 2, 2, 3)
t[0] # renvoie 1
t.count(2) # renvoie 2
t.index(2) # renvoie 1




# DICTIONNAIRES
dico = dict() # Création d'un dictionnaire vide
dico = {"nom": "Dupont", "prenom": "Jean", "age": 30} # Création d'un dictionnaire avec des valeurs
dico['nom'] # renvoie Dupont ( la clé )
dico.get('nom') # renvoie Dupont ( la clé ) et None si jamais la clé n'existe pas

dico['Sexe'] = 'M' # Ajout
item = dico.pop('nom') # Supprime la clé et renvoie la valeur

for key in dico:
    print(key, dico[key])

clef = dico.keys() # Renvoie les clés

for value in dico.values():
    print(value)

# Création d'un dictionnaire par compréhension    

liste_de_nombres = [1, 2, 3]
liste_de_lettres = ['a', 'b', 'c']

resultat = zip(liste_de_nombres, liste_de_lettres)

for element in resultat:
    print(element)
# Renvoie [(1, 'a'), (2, 'b'), (3, 'c')]
#dictionnaire = {cle: valeur for cle, valeur in zip(liste_de_cles, liste_de_valeurs)}
# renvoie {1: 'a', 2: 'b', 3: 'c'}




# SETS (pas de doublons)
s = set() # Création d'un ensemble vide
s = {1, 2, 3}
t = {3, 4, 5}
s.add(4) # Ajoute 4 à l'ensemble
s.remove(2) # Supprime 2 de l'ensemble
s.discard(2) # Supprime 2 de l'ensemble si il existe
union_set = s.union(t) # Renvoie l'union de s et t
intersection_set = s.intersection(t) # Renvoie l'intersection de s et t
difference_set = s.difference(t) # Renvoie la différence de s et t
s.update({5,6,7}) # Ajoute 5, 6 et 7 à l'ensemble s




# FROZENSETS
fs = frozenset([1, 2, 3]) # Création d'un ensemble immuable
fs.add(4) # Lève une exception car l'ensemble est immuable




# STRINGS
s = "Bonjour : Lue"
s[0] # renvoie B
s[1:3] # renvoie on
s.upper() # renvoie BONJOUR : LUE
s.lower() # renvoie bonjour : lue
s.startswith("B", 0, 1) # renvoie True car B est à l'indice 0 et on regarde de l'indice 0 à 1
#utiliser join:
s = "Bonjour : Lue"
s2 = s.split(":") # ['Bonjour ', ' Lue']
s3 = ":".join(s2) # renvoie Bonjour : Lue de type str
#utiliser isdigit, isalpha, isalnum, isspace:
s = "123"
s.isdigit() # renvoie True
s = "abc"
s.isalpha() # renvoie True
s = "123abc"
s.isalnum() # renvoie True car il y a des chiffres et des lettres
s = " "
s.isspace() # renvoie True
#utiliser index:
s = "Bonjour : Lue"
s.index("B") # renvoie 0
s.partition(":") # renvoie ('Bonjour ', ':', ' Lue') qui est un tuple
s.strip() # enlève les espaces au début et à la fin
s.replace(" ", "") #enleve tous les espaces
s.lstrip() # enlève les espaces au début
s.rstrip() # enlève les espaces à la fin
s.palindrome() # renvoie False



# FILES
f = open("fichier.txt", "r") # Ouverture en lecture seule
f = open("fichier.txt", "w") # Ouverture en écriture seule
lines = f.readlines() # Renvoie une liste contenant toutes les lignes du fichier: ['ligne 1\n', 'ligne 2\n']
line = f.readline() # Renvoie la ligne suivante du fichier, si on l'appelle plusieurs fois, renvoie les lignes suivantes
line = f.read() # f.read() renvoie tout le contenu du fichier sous forme de chaîne de caractères
f.close() # Ferme le fichier


# DYNAMIC PROGRAMMING
# C'est quoi la prgrammation dynamique?
# La programmation dynamique est une méthode pour résoudre des problèmes en décomposant en sous-problèmes.
#comment ça marche?
# On résout les sous-problèmes une seule fois et on stocke leurs solutions.
# On utilise ensuite ces solutions pour résoudre des problèmes plus grands.
# Pourquoi utiliser la programmation dynamique?
# La programmation dynamique est utile pour résoudre des problèmes qui ont des sous-problèmes répétitifs.
# exemple :
# La suite de Fibonacci est un bon exemple de problème qui peut être résolu avec la programmation dynamique.
# La suite de Fibonacci est définie comme suit :
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)
# Pour résoudre F(n), nous devons résoudre F(n-1) et F(n-2).
# Cependant, si nous résolvons F(n-1) et F(n-2) plusieurs fois, cela devient inefficace.
# La programmation dynamique nous permet de résoudre F(n-1) et F(n-2) une seule fois et de stocker leurs solutions.
# en python : 
def fibonacci(n):
    memo = {}
    def fib(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
    return fib(n)

 
# Définition d'une classe
class Chien:
    # Constructeur (appelé lors de la création d'un nouvel objet)
    def __init__(self, nom, race):
        self.nom = nom  # Attribut d'instance
        self.race = race  # Attribut d'instance

    # Méthode de la classe
    def aboyer(self):
        print(f"{self.nom} aboie : Woof!")

# Création d'objets (ou instances) de la classe
chien1 = Chien("Max", "Labrador")
chien2 = Chien("Bella", "Bulldog")

# Utilisation des méthodes de l'objet
chien1.aboyer()  # Affiche : Max aboie : Woof!
chien2.aboyer()  # Affiche : Bella aboie : Woof!


#FONCTIONS PYTHON
"""
#4 fonctions python
1- pprint (import)
pprint() est une fonction qui permet d'afficher des objets de manière plus lisible.

2- any()
any() est une fonction qui renvoie True si au moins un élément d'un itérable est vrai.
any(num > 0 for num in [1, 2, 3, -1]) # renvoie True mais False si tous les nombres sont négatifs
 
3- all()
all() est une fonction qui renvoie True si tous les éléments d'un itérable sont vrais.
all(num > 0 for num in [1, 2, 3, -1]) # renvoie False car -1 est négatif

4- enumerate()
enumerate() est une fonction qui renvoie un objet énuméré.
for i, j in enumerate([1, 2, 3]):
    print(i, j) # 0 1, 1 2, 2 3 

"""


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

### L'async en python :
# L'asynchrone est un modèle de programmation qui permet à votre code de gérer
# plusieurs tâches "simultanément" sans avoir besoin de multiples threads.
# pratique pour les requêtes réseau et l'accès au fichiers.
# sync : les opés bloquent jusqu'a etre effectué, async : l'inverse
# Coroutines: Fonctions spéciales qui peuvent suspendre leur exécution et la reprendre plus tard
# Event Loop: Le moteur qui exécute les coroutines et gère les tâches asynchrones

import asyncio

async def faire_cafe():
    print("Préparation du café...")
    await asyncio.sleep(3)
    print("Café prêt!")
    return "Café"

async def faire_toast():
    print("Préparation des toasts...")
    await asyncio.sleep(2)
    print("Toasts prêts!")
    return "Toasts"

async def petit_dejeuner():
    # Exécute les deux tâches en parallèle
    resultats = await asyncio.gather(
        faire_cafe(),
        faire_toast()
    )
    print(f"Petit déjeuner servi: {', '.join(resultats)}")

asyncio.run(petit_dejeuner())



# Iterateurs et générateurs
lst = [10, 20, 30]
it = iter(lst)   # on crée un itérateur sur la liste

print(next(it))  # → 10
print(next(it))  # → 20
print(next(it))  # → 30
# print(next(it))  # StopIteration (plus rien à donner)


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
