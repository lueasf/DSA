# Letter Combinations of a Phone Number : Amazon

# Sur les anciens téléphone : 2 = a ou b ou c etc.
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def letterCombination(digits):
    if digits == "":
        return []
    
    dico = {"2": "abc","3": "def",
            "4": "ghi","5": "jkl",
            "6": "mno","7": "pqrs",
            "8": "tuv","9": "wxyz"}
    output = []

    def backtrack(combination, next_d):
        if not next_d:
            output.append(combination)
            return 
        for letter in dico[next_d[0]]:
            backtrack(combination + letter, next_d[1:])

    backtrack("", digits)
    return output

print(letterCombination("23"))


"""
                            backtrack("", "23")
                             /          |                     |
             backtrack("a", "3")   backtrack("b", "3")   backtrack("c", "3")
             /          |         \          |     \                  |          
backtrack("ad", "")   backtrack("ae", "")   ...          backtrack("cf", "")
      |                   |                                      |
   output.append       output.append                            output.append
         return             return                                    return

"""