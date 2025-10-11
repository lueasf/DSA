#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<long long> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        sort(a.begin(), a.end());
        long long max_diff = 0;
        for (int i = 0; i < n; i += 2) {
            long long current_diff = a[i + 1] - a[i];
            max_diff = max(max_diff, current_diff);
        }
        cout << max_diff << endl;
    }
    return 0;
}