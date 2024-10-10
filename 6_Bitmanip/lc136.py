# single number 
# indice : utiliser xor bit a bit (ou exclusif), vaut 1 si les deux nombres sont différents.
# xor de 3 et 5 en binaire vaut 0b011 ^ 0b101 = 0b110 = 6

def singleNumber(self, nums):
    res = 0
    for i in nums:
        res = i ^ res
    return res
        