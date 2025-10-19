// C. No Cost Too Great (Easy Version)

#include <bits/stdc++.h>
using namespace std;

vector<int> unique_factors(long long x) {
    vector<int> f;
    for (long long d = 2; d * d <= x; ++d) {
        if (x % d == 0) {
            f.push_back((int)d);
            while (x % d == 0) x /= d;
        }
    }
    if (x > 1) f.push_back((int)x);
    return f;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<long long> a(n), b(n);
        for (auto &x : a) cin >> x;
        for (auto &x : b) cin >> x; 

        unordered_map<int,int> seen;
        bool ok0 = false, ok1 = false;

        for (auto x : a) {
            for (int p : unique_factors(x))
                if (++seen[p] >= 2) { ok0 = true; break; }
            if (ok0) break;
        }
        if (ok0) { cout << 0 << "\n"; continue; }

        for (auto x : a) {
            for (int p : unique_factors(x + 1))
                if (seen.count(p)) { ok1 = true; break; }
            if (ok1) break;
        }

        cout << (ok1 ? 1 : 2) << "\n";
    }
}
