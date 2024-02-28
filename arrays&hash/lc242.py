# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s,t):
    sl = []
    for i in s:
        sl.append(i)
    for i in t:
        if i not in sl:
            return False
        else :
            sl.remove(i)
    return (sl==[])

#mieux:
def isAnagram(s: str, t: str):
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    return sorted_s == sorted_t