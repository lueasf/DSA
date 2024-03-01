# étant donné une str, renvoyez la taille du dernier mot sachant qu'il y a des espaces en fin de chaîne et des tabulations

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()  # Supprime les espaces en fin de chaîne
        L = s.split(" ")
        if not L[-1]:
            L.pop() 
        return len(L[-1])  # Retourne la longueur du dernier mot
