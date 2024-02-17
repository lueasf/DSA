# trier par occurence une str 

class Solution:
    def frequencySort(self, s: str) -> str:
        occ = {}
        res = ""
        for lettre in s:
            if lettre not in occ:
                occ[lettre] = 1
            else:
                occ[lettre] += 1
        sorted_occ = sorted(occ.items(), key=lambda x: x[1], reverse=True)
        """key=lambda x: x[1]: Cela signifie que les éléments de la séquence sont triés en 
        fonction de leur deuxième élément (ici l'occ dans le tuple)."""

        for lettre, count in sorted_occ: # car sorted_occ est une LISTE DE TUPPLES
            res += lettre * count
        return res
    
#exemples de key : 
people = [{'name': 'Alice', 'age': 30},{'name': 'Bob', 'age': 25},{'name': 'Charlie', 'age': 35}]
sorted_people = sorted(people, key=lambda x: x['age']) 
# renvoie [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

strings = ['apple', 'banana', 'orange', 'kiwi']
sorted_strings = sorted(strings, key=len)
# renvoie ['kiwi', 'apple', 'banana', 'orange']

data = [(1, 'apple'), (3, 'banana'), (2, 'orange')]
sorted_data = sorted(data, key=lambda x: x[1])
# renvoie [(1, 'apple'), (3, 'banana'), (2, 'orange')]