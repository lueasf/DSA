#include <vector>
#include <algorithm>

class Solution {
    public:
        long long mostPoints(vector<vector<int>>& questions) {
            int n = questions.size();
            std::vector<long long> dico(n + 1, 0);
    
            for (int i = n - 1; i >= 0; i--){
                int points = questions[i][0];
                int bp = questions[i][1];
                int next = 1 + i + bp;
    
                long long take = points + ( next < n ? dico[next] : 0);
                long long pass = dico[i+1];
                dico[i] = std::max(take, pass);
            }
            return *std::max_element(dico.begin(), dico.end());
        }
    };