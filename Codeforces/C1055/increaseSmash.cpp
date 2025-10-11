#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        set<int> distinct_elem;
        for (int i = 0; i < n; ++i) {
            int a;
            cin >> a;
            distinct_elem.insert(a);
        }
        int k = distinct_elem.size();
        if (k == 1) {
            cout << 1 << endl;
        } else {
            cout << 2 * k - 1 << endl;
        }
    }
    return 0;