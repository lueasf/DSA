# STRUCTURES DE DONNÉES


# LISTES
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

for key, value in dico.items():
    print(key, value)

# COMPREHENSION DE LISTE
