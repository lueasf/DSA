#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); // make I/O faster
    cin.tie(nullptr); // disable automatic flushing of cout before cin

    int t;
    cin >> t;
    while (t--) {
        long long k, x;
        cin >> k >> x;
        cout << (x << k) << "\n"; // res = x * (2^k) as 2*x is possibly the previous term
    }
    return 0;
}