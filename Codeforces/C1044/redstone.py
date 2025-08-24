# A. Redstone? on Codeforces Round 1044 (Div. 2) Aug/24/2025

import sys

def solve():
    data = sys.stdin.read().strip().split()
    idx = 0
    
    t = int(data[idx]); idx += 1
    out = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        seen = set()
        ok = False
        for _ in range(n):
            x = int(data[idx]); idx += 1
            if not ok:
                if x in seen:
                    ok = True
                else:
                    seen.add(x)
        out.append("YES" if ok else "NO")
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

"""We want the last geer to have a speed of 1 tpm. By recursivity, we can see that:
speed of the last gear = number of teeth of the first gear / number of teeth of the last gear.
The final condition is that : n theet 1st = n teeth last !.
Therefore, we only need to check if there is a gear with the same number of teeth as the first one."""