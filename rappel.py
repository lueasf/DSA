# STRUCTURES DE DONNÉES


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
# ENSEMBLES


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

# SETS
# FROZENSETS
# STRINGS
s = "Bonjour : Lue"
s[0] # renvoie B
s[1:3] # renvoie on
s.upper() # renvoie BONJOUR : LUE
s.startswith("B") # renvoie True
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
