#1 )

def loadDictionnary(filename):
    f = open(filename, 'r')
    L = [[]]
    index = 0
    for char in f.read(): # parcourt char par char car c'est une str
        if char == '\n':
            L.append([])
            index += 1
        else:
            L[index].append(char)

    f.close()
    return L

print(loadDictionnary('dico.txt'))

#2 )

def isMember(word, dictionnary):
    return word in dictionnary

print(isMember(['a','n'],[['a','n'],['b','a','n']]))

#3 )

def nextLevelShrink(word):
    res = []
    for i in range(len(word)):
        char = word.pop(i)
        res.append(word.copy())
        word.insert(i, char)
    return res

print(nextLevelShrink(['b','a','n']))

#4 )

def superCoolWord(word:list[str], dictionary: list[list[str]]) -> bool:
    w = word.copy()
    while w in dictionary:
        next = nextLevelShrink(w)
        for mot in next:
            if mot in dictionary:
                w = mot
                break
        return len(w) == 1
    return False

print(superCoolWord(['a','n'],[['a','n'],['a'],['b','a','n']]))


#5 )
def superCoolDictionnary(dico, length):
    res = []
    for w in dico:
        if superCoolWord(w, dico) and len(w) == length:
            res.append(w)
    return res

print(superCoolDictionnary([['a','n'],['a'],['b','a','n']],2))

#6 )
def superCoolChain(word, dico):
    res= []

    def backtrack(curr):
        if len(curr) == 1 and curr in dico:
            res.append(curr)
            return True
        
        if curr in dico:
            res.append(curr.copy())

            for reduit in nextLevelShrink(curr):
                if backtrack(reduit):
                    return True
            res.pop()

        return False
        

    if backtrack(word):
        return res
    else :
        return []
        
print(superCoolChain(['b','a','n','a'], [['a'],['a', 'n'],['b','o'],['b', 'a', 'n'],['b','o','o'], ['b', 'a', 'n', 'a'], ['b', 'a', 'n', 'a', 'n'], ['b', 'a', 'n', 'a', 'n', 'a']]))