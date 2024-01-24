# Trouver l'index de l'occurence dans la chaine de caractère:

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack)):
            if haystack.startswith(needle, i, i + n):
                return i
        return -1