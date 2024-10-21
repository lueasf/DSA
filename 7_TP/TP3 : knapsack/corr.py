from typing import List, Tuple

def take(object_index: int, bag):
    bag[object_index] = True
    return bag

def drop(object_index, bag):
    bag[object_index] = False
    return bag

def weight(bag, weights):
    L = [weight*bag[index] for index,weight in enumerate(weights)] 
    return sum(L)

#1 dans cet exercice, on cherche à trouver une solution optimale, on ne cherche pas à toutes les trouver
# on ne fait pas de copie de la liste bag, on la modifie directement
def find_one_best_sol_rec( capacity: int, weights, depth : int, bag: List[bool], best_bag: List[bool]):
    if weight(bag, weights) >= weight(best_bag, weights):  # si la valeur du sac courant est supérieure à la meilleure valeur trouvée, comme on cherche à maximiser la valeur
        best_bag = bag 

    if depth >= len(weights): # si on a parcouru tous les objets
        return best_bag
    
    if weights[depth] <= capacity:
        bag = take(depth,bag)
        best_bag = find_one_best_sol_rec(capacity - weights[depth], weights, depth +1, bag, best_bag)
        bag = drop(depth,bag)
    else:
        best_bag = find_one_best_sol_rec(capacity, weights, depth + 1, bag, best_bag) # on ne prend pas l'objet

    return best_bag

def find_one_best_sol(capacity: int, weights: List[int]):
    return find_one_best_sol_rec(capacity, weights, 0, [False]*len(weights), [False]*len(weights))

#2 dans cet exercice, on cherche à trouver une solution optimale, on ne cherche pas à toutes les trouver
def generic_find_one_best_sol_rec(capacity, weights, depth, bag, best_bag):
    if depth >= len(weights):
        return best_bag
    
    for action in [True, False]:
        old_val = bag[depth]

        bag[depth] = action

        if weight(bag, weights) <= capacity:
            if weight(bag, weights)  >= weight(best_bag,weights):
                best_bag = list(bag) # copie du sac

            best_bag = generic_find_one_best_sol_rec(capacity, weights, depth+ 1, bag, best_bag)

        bag[depth] = old_val

    return best_bag

def find_one_best_sol(capacity, weights):
    return generic_find_one_best_sol_rec(capacity, weights, 0, [False]*len(weights), [False]*len(weights))