def dichotomic_search(tab, low, high, element):
    if low > high:
        return -1
    mid = (low + high) // 2
    
    if tab[mid] == element:
        return mid
    
    elif tab[mid] > element:
        return dichotomic_search(tab, low, mid - 1, element)
    
    else:
        return dichotomic_search(tab, mid + 1, high, element)

def dichotomic_search_iterative(tab, element):
    low = 0
    high = len(tab) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if tab[mid] == element:
            return mid
        elif tab[mid] > element:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1


# Ex2
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

