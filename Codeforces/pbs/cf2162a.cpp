#include <bits/stdc++.h>
using namespace std;

int main() {

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int m = 0;
        for (int i = 0; i < n; i++){
            int x;
            cin >> x;
            m = max(m, x);
        }
        cout << m << "\n";
    }
    return 0;
}
