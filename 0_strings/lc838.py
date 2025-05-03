# Push Dominoes (Medium)

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dots = 0 # nb consécutifs de "."
        rs = 0 # nb conséc de 'R'
        ans = ""
        for i in dominoes:
            if i == 'L':
                ans += "R" * rs
                if rs and dots:
                    ans += "R" * (dots // 2)
                    ans += "." * (dots % 2)
                    ans += "L" * (dots // 2)
                elif dots:
                    ans += "L" * dots
                ans += "L"
                rs = 0
                dots = 0

            elif i == '.':
                dots += 1

            else:
                if not rs and dots:
                    ans += "." * dots
                    dots = 0
                elif rs and dots:
                    ans += "R" * rs
                    ans += "R" * dots
                    dots = 0
                    rs = 0
                rs += 1

        if rs and dots:
            ans += "R" * rs
            ans += "R" * dots
        elif dots:
            ans += "." * dots
        elif rs:
            ans += "R" * rs
        return ans
