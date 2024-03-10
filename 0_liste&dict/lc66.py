# un nb est representé par une liste : ajouter 1 au nb et renvoyer la liste:

# [9] -> [1,0]
# [9,9] -> [1,0,0]
# [1,2,3] -> [1,2,4]

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        nbneuf = 0
        for i in range(1,len(digits) + 1):
            if digits[-i] == 9:
                nbneuf += 1
                digits[-i] = 0
            else :
                break
        if len(digits) > nbneuf:
            digits[len(digits) - nbneuf -1] += 1
            return digits
        else:
            return [1] + digits
        

# MIEUX
def plusOne(digits):
    for i in reversed(range(len(digits))):
        if digits[i] != 9:
            digits[i] +=1
            return digits
        digits[i] = 0
    return [1] + digits