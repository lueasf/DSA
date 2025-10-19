// A. Mex Partition from Codeforces Round #1058 (Div. 2)

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        vector<int> freq(102, 0);

        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            freq[x]++;
        }

        int mex = 0;
        while (freq[mex] > 0) ++mex;
        cout << mex << '\n';
    }
    return 0;
}