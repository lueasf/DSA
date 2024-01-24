# le plus long préfixe commun des strings d'une liste

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    base = strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            if (i == len(word)) or base[i] != word[i]:
                return base[:i]
    return base