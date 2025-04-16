# Count Good Triplets in an Array (Hard)

# Un arbre de Fenwick (ou Binary Indexed Tree, BIT) est une structure de données efficace pour :
# - Calculer des sommes des éléments d'un tableau jusqu'à un indice donné. de i a j.
# Complexité : O(log² n), mieux qu'un simple parcours pour une range calc

# on encode les indices en binaire, on commence a l'index 1
# on prends tout ceux qui commence par 1 en binaire (rightwise), puis 1 encore a l'indice 3
# rightwise, et on somme 2 valeurs, puis 4, etc. de manière exponentielle

class FenwickTree:
	def __init__(self, size):
		self.tree = [0] * (self.size + 1)

	def update(self, index, delta):
		index += 1
		while index <= len(self.tree) -1:
			self.tree[index] += delta
			index += index & -index

	def query(self, index):
		index += 1
		res = 0
		while index > 0:
			res += self.tree[index]
			index -= index & -index
		return res

#### Binary Search
# bisect , permet de faire du bs et des insertions triées dans des listes déja ordonnées.
bisect.bisect_left(a,x) # trouve l'indice où insérer x dans la liste triée a
# si x existe déjà, retourne l'indice le plus à gauche, pareil pour bisect_right

bisect.insort_left(a,x) # insère x dans a pour conserver l'ordre.
bisect.insort_right(a,x) # pareil mais après les doublons eventuels.

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0

        """
        nums1 = [2,0,1,3], indice1 = [1,2,0,3] car 0 est en 1 dans nums1, 1 est en 2 .. etc
        nums2 = [0,1,2,3]
        nums1_transformé : on remmplace chaque el de nums2 par sa position dans nums1 :
            nums2 = [0, 1, 2, 3] → [indices[0], indices[1], indices[2], indices[3]]

        on transforme nums2 pour qu'elle encode les positions ds nums1,  en gardant l'ordre de nums2.
        """
        indices = [0] * len(nums1)
        for i, num in enumerate(nums1):
            indices[num] = i

        for i, num in enumerate(nums2):
            nums1[i] = indices[num]


        arr = SortedList() # tri auto

        for i, num in enumerate(nums1[::-1]):
            index = arr.bisect(num) # nb d'élément vu < num à gauche car c'est lindice ou num serait inséré
            # i - bisect = nb d'élément vu > num à droite
            count += (i - index) * (num - index) # num - bisect = nb d'el < num restants à gauche
            # count compte tt les triplets ou num est au milieu
            arr.add(num)

        return count
