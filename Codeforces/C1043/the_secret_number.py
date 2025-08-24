# B. The Secret Number on Codeforces Round 1043 (Div. 3) Aug/21/2025

import sys

def get_int():
    return int(sys.stdin.readline())

def solve():
    n = get_int()
   
    sol = []
    pow_10 = 10

    while True:
        d = 1 + pow_10
        if d > n:
            break
        if n % d == 0:
            x = n // d
            sol.append(x)

        pow_10 *= 10
    if not sol:
        print(0)
    else:
        sol.reverse()
        print(len(sol))
        print(*sol)


def main():
    num_test_cases = get_int()
    for i in range(num_test_cases):
        solve()

if __name__ == "__main__":
    main()

"""Vadim choose a positive integer x.
He "attaches" k>0 zeros to the end to create a new number y. Then n = x + y. The
goal is to find all possible x, given n.
y = x * 10^k, therefore n = x + x * 10^k = x * (1 + 10^k).
We have to solve : x = n / (1 + 10^k) for k >= 1 and x > 0.
We iterate over k, until (1 + 10^k) > n, as x >= 1."""