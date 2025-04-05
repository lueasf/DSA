#include <vector>
#include <algorithm> // Pour std::min

class Solution {
public:
    vector<int> minCosts(vector<int>& cost) {        
        vector<int> res;
        res.push_back(cost[0]);

        for (int i = 1; i < cost.size(); i++) { 
            res.push_back(min(res[i-1], cost[i])); 
        }
        return res;
    }
};