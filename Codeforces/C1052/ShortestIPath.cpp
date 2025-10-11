// A. Shortest Increasing Path

#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        long long x, y;
        cin >> x >> y;

        long long ans;
        if (x == y) {
            ans = -1;
        } else if (y > x) {
            ans = 2;
        } else {
            if (y == 1) ans = -1;
            else if (x >= y + 2) ans = 3;
            else ans = -1;
        }

        cout << ans << "\n";
    }
    return 0;
}