// A. Notelock

#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n, k;
        string s;
        cin >> n >> k >> s;

        vector<int> ones;
        for (int i = 0; i < n; i++){
            if (s[i] == '1') {
                ones.push_back(i);
            }
        }

        if (ones.size() == 0){ cout << 0 << "\n"; continue;}

        int ans = 1;
        int last = ones[0];
        for (int i = 1; i < ones.size(); i++){
            if (ones[i] - last >= k){
                ans++;
                last = ones[i];
            } else {
                last = ones[i];
            }
        }
        cout << ans << "\n";
        
    }
    return 0;
}