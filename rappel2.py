# BACKTRACKING
# C'est un type de parcours d'arbe
# on à un problème et on trouve une solution
# EXEMPLE : résoudre un sudoku







# DYNAMIC PROGRAMMING
# C'est quoi la prgrammation dynamique?
# La programmation dynamique est une méthode pour résoudre des problèmes en décomposant en sous-problèmes.
#comment ça marche?
# On résout les sous-problèmes une seule fois et on stocke leurs solutions.
# On utilise ensuite ces solutions pour résoudre des problèmes plus grands.
# Pourquoi utiliser la programmation dynamique?
# La programmation dynamique est utile pour résoudre des problèmes qui ont des sous-problèmes répétitifs.
# exemple :
# La suite de Fibonacci est un bon exemple de problème qui peut être résolu avec la programmation dynamique.
# La suite de Fibonacci est définie comme suit :
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)
# Pour résoudre F(n), nous devons résoudre F(n-1) et F(n-2).
# Cependant, si nous résolvons F(n-1) et F(n-2) plusieurs fois, cela devient inefficace.
# La programmation dynamique nous permet de résoudre F(n-1) et F(n-2) une seule fois et de stocker leurs solutions.
# en python : 
def fibonacci(n):
    memo = {}
    def fib(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo[n]
    return fib(n)



# MEMOIZATION
# RECURSION
# RECURSIVE DYNAMIC PROGRAMMING