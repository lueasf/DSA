
def loadDictionnary(fn):
    f = open(fn,"r")
    L = [[]]
    index = 0
    for char in f.read():
        if char =='\n':
            L.append([])
            index += 1
        else:
            L[index].append(char)
    return L
# print(loadDictionnary("dico.txt"))

def isMember(w,d):
    return w in d
# print(isMember(['a','n'],[['a'], ['a', 'n'], ['b', 'a', 'n'], ['b', 'a', 'n', 'a'], ['b', 'a', 'n', 'a', 'n'], ['b', 'a', 'n', 'a', 'n', 'a']]))


def nextLevelShrink(w):
    L = []
    for i in range(1,len(w)):
        L.append(w[0:i-1]+w[i:])
    for i in range(1,len(w)):
        if w[0:i]+w[i+1:] not in L:
            L.append(w[0:i]+w[i+1:])
    return L
# print(nextLevelShrink(['b', 'a', 'n','o','p','m']))


def superCoolWord(word, dico):
    if len(word) == 1:
        return word in dico
    else:
        for i in range(len(word)):
            if word in dico:
                L = nextLevelShrink(word)
                for i in L:
                    if i in dico:
                        word = i
        return (len(word) == 1)
# print(superCoolWord(['a'],[['a'],['o'],['a', 'n'],['b','o'], ['b', 'a', 'n'],['b','o','o'],['b', 'a', 'n', 'a'], ['b', 'a', 'n', 'a', 'n'], ['b', 'a', 'n', 'a', 'n', 'a']]))


def superCoolDico(dico, l):
    L = []
    for w in dico:
        if len(w) == l:
            if superCoolWord(w, dico):
                L.append(w)
    return L
#print(superCoolDico([['o'],['a'],['a', 'n'],['b','o'],['b', 'a', 'n'],['b','o','o'], ['b', 'a', 'n', 'a'], ['b', 'a', 'n', 'a', 'n'], ['b', 'a', 'n', 'a', 'n', 'a']], 3))


def superCoolChain(word, dico):
    res= []
    if len(word) == 1 and word in dico:
        return [word]
    else:
        for i in range(len(word)):
                if word in dico:
                    res.append(word)
                    L = nextLevelShrink(word)
                    for i in L:
                        if i in dico:
                            word = i
                            break
                else: 
                    return []
        return res
            
print(superCoolChain(['b','a','n','a'],[['a'],['a', 'n'],['b','o'],['b', 'a', 'n'],['b','o','o'], ['b', 'a', 'n', 'a'], ['b', 'a', 'n', 'a', 'n'], ['b', 'a', 'n', 'a', 'n', 'a']]))
