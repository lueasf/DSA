# STRUCTURES DE DONNÉES #

"""
Listes dico modifiables, ensembles sans doublons, tuples non modifiables avec ordres.
L = [1,2], D = {1:2}, S = {1,2}, T = (1,2)
"""

# LISTES
L = [1, 2, 3]
L.append(4) # Ajoute 4 à la fin de la liste
L.insert(0, 0) # Ajoute 0 à l'indice 0

L.pop() # Supprime le dernier élément de la liste et renvoie la valeur
L.pop(0) # Supprime l'élément à l'indice 0 et renvoie la valeur
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

# TUPLES
t = (1, 2, 2, 3)
t[0] # renvoie 1
t.count(2) # renvoie 2
t.index(2) # renvoie 1

# DICTIONNAIRES
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
s.startswith("B", 0, 1) # renvoie True car B est à l'indice 0 et on regarde de l'indice 0 à 1
#utiliser join:
s = "Bonjour : Lue"
s2 = s.split(":") # ['Bonjour ', ' Lue']
s3 = ":".join(s2) # Bonjour : Lue
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
s.partition(":") # renvoie ('Bonjour ', ':', ' Lue')
s.strip() # enlève les espaces au début et à la fin
s.lstrip() # enlève les espaces au début
s.rstrip() # enlève les espaces à la fin
s.palindrome() # renvoie False

# FILES
f = open("fichier.txt", "r") # Ouverture en lecture seule
f = open("fichier.txt", "w") # Ouverture en écriture seule
lines = f.readlines() # Renvoie une liste contenant toutes les lignes du fichier
line = f.readline() # Renvoie la ligne suivante du fichier
f.close() # Ferme le fichier