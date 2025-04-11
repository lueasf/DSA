
# BYME
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            nb = str(i)
            if len(nb) % 2 != 0:
                continue
            length = len(nb) // 2
            if sum(list(map(int,(nb[:length])))) == sum(list(map(int,(nb[length:])))):
                count += 1
        return count

# Editorial
Since the high is bounded by 10 000, there is an elegant solution:

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for a in range(low, high + 1):
            if a < 100 and a % 11 == 0:
                res += 1
	    if 1000 <= a < 10000:
		left = a // 1000 + a % 1000 // 100
                right = a % 100 // 10 + a % 10
                if left == right:
                    res += 1
        return res

