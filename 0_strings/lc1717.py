
# byme
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        m = x if x > y else y
        total = 0
        s_list = list(s)
        
        i = 0
        while i < len(s_list) - 1:
            if m == x and s_list[i] == 'a' and s_list[i + 1] == 'b':
                total += x
                del s_list[i:i + 2]
                if i > 0:
                    i -= 1
            elif m == y and s_list[i] == 'b' and s_list[i + 1] == 'a':
                total += y
                del s_list[i:i + 2]
                if i > 0:
                    i -= 1
            else:
                i += 1
        
        i = 0
        while i < len(s_list) - 1:
            if m == x and s_list[i] == 'b' and s_list[i + 1] == 'a':
                total += y
                del s_list[i:i + 2]
                if i > 0:
                    i -= 1
            elif m == y and s_list[i] == 'a' and s_list[i + 1] == 'b':
                total += x
                del s_list[i:i + 2]
                if i > 0:
                    i -= 1
            else:
                i += 1
        
        return total