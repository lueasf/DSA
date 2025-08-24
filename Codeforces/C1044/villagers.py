# B. Villagers on Codeforces Round 1044 (Div. 2) Aug/24/2025

import sys

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0]); idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        g = list(map(int, data[idx:idx+n])); idx += n
        g.sort(reverse=True)
        ans = sum(g[0::2])
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

"""There are some villagers with grumpiness levels.
An operation on the 2 villagers (i,j) costs max(g[i], g[j]) grumpiness points.
And the grumpiness level decreases by the min(g[i], g[j]), leading to their friendship.
We get at least 1 zero every time (can lead to cost 0) so we need at least n/2 operations
to make all villagers friends.
We need to organize in decreasing order the villagers,
arrange them in pairs and sum the max of each pair (g1 + g3 + g5 + ...)."""