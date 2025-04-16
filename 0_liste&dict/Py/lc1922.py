# Count Good Numbers

# BYME (TIME LIMITTTTT)
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            sqr = int(num ** 0.5) + 1
            for i in range(2, sqr):
                if num % i == 0:
                    return False
            return True

        count = 0
        dig_min = 10 ** (n - 1)
        dig_max = 10 ** n

        for i in range(dig_min, dig_max):
            s = str(i)
            valid = True
            for j in range(len(s)):
                digit = int(s[j])
                if j % 2 == 0:
                    if digit % 2 != 0:
                        valid = False
                        break
                else:
                    if not is_prime(digit):
                        valid = False
                        break
            if valid:
                count += 1

        return count % (10**9 + 7)

# BYME, better, but  TIME LIMITTTT
class Solution:
    def countGoodNumbers(self, n: int) -> int:

        count = 0
        dig_min = 10 ** (n - 1)
        dig_max = 10 ** n

        for i in range(dig_min, dig_max):
            s = str(i)
            valid = True
            for j in range(len(s)):
                if j % 2 == 0:
                    if s[j] not in ["0","2","4","6","8"]:
                        valid = False
                        break
                else:
                    if s[j] not in ["2","3","5","7"]:
                        valid = False
                        break
            if valid:
                count += 1
        return count % (10 ** 9 + 7)

# WTH

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_positions = (n + 1) // 2  # Nombre de positions paires (0-based)
        odd_positions = n // 2         # Nombre de positions impaires
        return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD

# Indeed, the even are in [0,2,4,6,8]
# And the odd in [2,3,4,7]
# so we have 5**(event) * 4**(odd)
# which is even : n+1 // 2, odd :  n//2
