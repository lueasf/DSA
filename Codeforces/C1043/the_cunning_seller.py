# C. The Cunning Seller (easy) on Codeforces Round 1043 (Div. 3) Aug/21/2025

import sys

def get_int():
    return int(sys.stdin.readline())

def solve():
    n = get_int()
   
    total_cost = 0
    deal_type = 0
    pow_3 = 1

    while n > 0:
        nb_type = n % 3

        if nb_type > 0:
            cost_deal = (pow_3 * 3) + deal_type * (pow_3 // 3)
            total_cost += nb_type * cost_deal

        n //= 3
        deal_type += 1
        pow_3 *= 3

    print(total_cost)

def main():
    num_test_cases = get_int()
    for _ in range(num_test_cases):
        solve()

if __name__ == "__main__":
    main()