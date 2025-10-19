// B. Make it Zigzag 

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        vector<long long> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];

        vector<long long> pref(n); // prefix max
        pref[0] = a[0];
        for (int i = 1; i < n; i++) pref[i] = max(pref[i - 1], a[i]);

        long long ans = 0;
        for (int j = 0; j < n; j+= 2){
            long long cap;
            if (j == 0){
                cap = pref[1];
            } else {
                cap = pref[j - 1];
            }
            long long target = cap - 1;
            if (a[j] > target) ans += (a[j] - target);
        }

        cout << ans << "\n";
        
    }
    return 0;
}