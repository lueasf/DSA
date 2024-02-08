# un nb est representé par une liste : ajouter 1 au nb et renvoyer la liste:

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
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