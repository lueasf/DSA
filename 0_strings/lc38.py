# Count and Say (Medium)

class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for j in range(n-1):
            current = ""
            count = 1
            for e in range(1,len(result)):
                if result[e] == result[e - 1] :
                    count += 1
                else:
                    current += str(count) + result[e - 1]
                    count = 1
            current += str(count) + result[-1]
            result = current
        return result
