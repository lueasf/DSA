# Add Binary : Amazon & Google

# la somme en binaire de str

# FAV

def addBinary( a: str, b: str) -> str:
    a = int(a,2)
    b = int(b,2)
    return bin(a+b)[2:]

print(addBinary("11","1"))  # 100