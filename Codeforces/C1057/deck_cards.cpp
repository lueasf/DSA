#include <iostream>
#include <string>
using namespace std;

int main() {
    int t; 
    cin >> t;
    while (t--) {
        int n, k; 
        cin >> n >> k;
        string s; 
        cin >> s;

        int a = 0, b = 0, c = 0; // a='0' (top), b='1' (bottom), c='2' (flex)
        for (char ch : s) {
            if (ch == '0') ++a;
            else if (ch == '1') ++b;
            else ++c;
        }

        string ans(n, '-');
        int len = n - k;

        if (len > 0){
            // [L_union, R_union]
            int L_union = a, R_union = n -1 -b;
            int L_inter = a + c, R_inter = n -1 -b -c;

            if (L_union <= R_union){
                for (int i = L_union; i <= R_union; ++i) ans[i] = '?';
            }
            if (L_inter <= R_inter){
                for (int i = L_inter; i <= R_inter; ++i) ans[i] = '+';
            }
        }

        cout << ans << '\n';
    }
    return 0;
}