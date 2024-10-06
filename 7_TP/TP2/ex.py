def putInBag(sac, index):
    sac.append(index)  # Ajoutez l'index de l'objet au lieu du poids

def removeFromBag(sac, index):
    if index in sac:
        sac.remove(index)

def isTaken(sac, index):
    return index in sac

def ks_value(sac, objets, valeurs):
    res = 0
    for i in sac:  # i est maintenant un index
        res += valeurs[i]  # Accéder aux valeurs avec l'index
    return res

def ks_search(sac, taille, index, objets, valeurs):
    if index >= len(objets):
        return ks_value(sac, objets, valeurs)

    objet_courant = objets[index]
    val_incluse = 0
    if objet_courant <= taille:
        sac_objet = ks_duplicate(sac)  # Dupliquer le sac
        putInBag(sac_objet, index)  # Ajouter l'index de l'objet au sac
        val_incluse = ks_search(sac_objet, taille - objet_courant, index + 1, objets, valeurs)
    
    val_exclue = ks_search(sac, taille, index + 1, objets, valeurs)
    return max(val_incluse, val_exclue)

def ks_duplicate(sac):
    return sac.copy()  # Les modifications sur la copie n'affectent pas l'original
 
objets = [5, 4, 3, 12]  # Poids des objets
valeurs = objets 
capacité_maximale = 11
sac = []

# Appeler la fonction
meilleure_valeur = ks_search(sac, capacité_maximale, 0, objets, valeurs)
print("Meilleure valeur dans le sac à dos :", meilleure_valeur)
