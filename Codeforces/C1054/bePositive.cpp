#include <iostream>
using namespace std;


int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, a, neg = 0, zero = 0;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> a;
            if (a == 0) zero++;
            else if (a < 0) neg++;
        }
        int ops = zero;
        if (neg % 2 != 0) {
            ops += 2;
        }
        cout << ops << "\n";
    }
    return 0;
}