# A. Homework on Codeforces Round 1043 (Div. 3) Aug/21/2025

import sys
from collections import deque

def solve():
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().strip()
    m = int(sys.stdin.readline())
    b = sys.stdin.readline().strip()
    c = sys.stdin.readline().strip()
    res_deque = deque(a)
   
    for i in range(m):
        if c[i] == 'V':
            res_deque.appendleft(b[i])
        else:
            res_deque.append(b[i])
           
    print("".join(res_deque))

def main():
    num_test_cases = int(sys.stdin.readline())
    for _ in range(num_test_cases):
        solve()

if __name__ == "__main__":
    main()