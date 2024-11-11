# O(n * m * sqrt(n)) 
# not opti

from cmath import sqrt

class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        def is_prime(n):
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True


        prev = 0
        for n in nums:
            upper = n - prev

            largest_prime = 0
            for i in reversed(range(2, upper )):
                if is_prime(i):
                    largest_prime = i
                    break

            if n - largest_prime <= prev:
                return False
            prev = n - largest_prime
        return True
