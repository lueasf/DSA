#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>

using namespace std;

class Solution {
    public:
        vector<int> partitionLabels(string s) {
            std::unordered_map<char, int> occ;
            int n = s.length();
    
            for (int i =0; i < n; i++){
                occ[s[i]] = i;
            }
    
            vector<int> res;
            int l = 0, r = 0;
    
            for (int i = 0; i < n ; i++){
                r = max(r, occ[s[i]]);
                if (i == r){
                    res.push_back(r - l + 1);
                    l = i + 1;
                }
            }
            return res;
    
        }
    };