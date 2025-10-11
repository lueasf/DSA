// A

#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        int n;
        cin >> n;
        int rem = n % 3;

        int add = (rem == 0) ? 0 : (3 - rem);
        cout << add << endl;
    }
    return 0;
}