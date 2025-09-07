#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    if (!(cin >> t)) return 0;

    while (t--){
        long long a, b;
        cin >> a >> b;

        // b is odd, 1LL is long long 1
        if (b & 1LL){
            if (a & 1LL){ 
                cout << ( a * b + 1 ) << "\n"; 
            } else {
                cout << -1 << "\n";
            }
            continue;
        }

        // b is even
        int f = __builtin_ctzll(b); // function that counts trailing zeros in binary representation of b (last bits that are 0)
        // if f == 1, b is multiple of 2 but not 4
        if ((a & 1LL) && f ==  1){
            cout << -1 << "\n";
            continue;
        }

        long long half = b >> 1; // b / 2
        cout << ( a * half + 2 ) << "\n";
    }
    return 0;
}

/*
a and b. Choose K that divides b. Then a' = a * k, b' = b / k. Maximize a' + b' even.
first, a'b' = ab. 

La somme qu’on maximise est : ak + b/k

Case A : b odd
-> b/k odd
- a even : a*k even + b/k odd = odd -> impossible
- a odd : a*k odd + b/k odd = even -> possible
Max k = b, so a' = ab , b' = 1 and S = ab + 1


Case B : b even
-> b can be divided by 2 so k = b/2 -> a' = a*(b/2), b' = 2 and S = a*(b/2) + 2
- a even : a*(b/2) even + 2 = even -> possible
- a odd : if b multiple of 4 -> (b/2) even -> a*(b/2) even + 2 = even -> possible
         if b multiple of 2 not 4 -> (b/2) odd -> a*(b/2) odd + 2 = odd -> impossible

Therefore : 
- b odd :
    - a odd -> S = ab + 1
    - a even -> -1
- b even :
    - a even -> S = a*(b/2) + 2
    - a odd :
        - b multiple of 4 -> S = a*(b/2) + 2
        - b ≡ 2 mod 4 -> -1
*/