# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


def groupAnagrams(strs):
    dict = {} 
    for s in strs:
        so ="".join(sorted(s)) #on recupère les str rangées sans les quotes
        if so not in dict:
                dict[so] = [s] 
        else:
            dict[so].append(s)
    return dict.values()
    
#BYME
def groupAnagrams2(strs):
    dico = dict()
    for i in range(len(strs)):
        sw = sorted(strs[i])
        sw = "".join(sw)
        if sw not in dico.keys():
            dico[sw] = [strs[i]]
        else:
            dico[sw].append(strs[i])
    return dico.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))