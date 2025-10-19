#include <bits/stdc++.h>
using namespace std;

// xor is 1 when x and y are different, 0 when they are the same
// look bits to bits : ni = bi xor bL-1-i
// can remove last zeros
// if L is odd, bL/2 must be 0

bool is_pal(const string &s){
    int n = (int)s.size();
    for (int i = 0, j = n - 1; i < j; ++i, --j)
        if (s[i] != s[j]) return false;
    return true;
    }

int main() {
    int t; 
    cin >> t;

    while (t--) {
        unsigned int n; 
        cin >> n;

        if (n == 0){
            cout << "YES\n";
            continue;
        }

        unsigned int k = __builtin_ctz(n);
        unsigned int m = n >> k; // n without trailing zeros

        string s;
        while (m > 0) {
            s = ((m & 1) ? '1' : '0') + s;
            m >>= 1;
        } // s is n in bin.

        if (s.empty()) s = "0";
        bool ok = is_pal(s) && ( (s.size() % 2 == 0) || (s[s.size()/2] == '0'));
        cout << (ok ? "YES\n" : "NO\n");
    }
    return 0;
}
