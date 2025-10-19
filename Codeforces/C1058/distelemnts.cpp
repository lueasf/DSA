#include <bits/stdc++.h>
using namespace std;

int main() {
    int t; 
    cin >> t;

    while (t--) {
        int n; 
        cin >> n;
        vector<long long> b(n + 1, 0); 
        for (int i = 1; i <= n; ++i) cin >> b[i];

        vector<int> a(n + 1, 0);
        int next = 1;

        for (int i = 1; i <= n; ++i) {
            long long d = b[i] - b[i - 1]; 
            if (d == i) {
                a[i] = next++;
            } else {
                int p = int(i - d); // d = i - p
                a[i] = a[p];
            }
        }

        for (int i = 1; i <= n; ++i) {
            if (i > 1) cout << ' ';
            cout << a[i];
        }
        cout << '\n';
    }
    return 0;
}

/*
We compute the values of b[i] to understand how the sequence evolves:

i	Subarrays ending at i	f() (distinct count)	Sum bi
1	[1]	1	1
2	[1,2], [2]	2 + 1	3
3	[1,2,2], [2,2], [2]	2 + 1 + 1	4

Now we look at the differences:
d1 = 1, d2 = 2, d3 = 1.

When d = i (for example d2 = 2), it means the new element a[i] is a completely new value that hasn’t appeared before → we assign a new label.
When d < i (for example d3 = 1), it means the element a[i] has already appeared earlier → we reuse an existing value.

To know which value to reuse, the code uses the formula d = i - p,
where p is the previous position of the same number.
So p = i - d tells us where that value last appeared.
*/
