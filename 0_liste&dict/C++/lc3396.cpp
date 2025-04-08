class Solution {
    public:
        int minimumOperations(std::vector<int>& nums) {
            int nb_op = 0;
             
            while (nums.size() > std::unordered_set<int>(nums.begin(), nums.end()).size()) {
    
                if (nums.size() >= 3) {
                    nums = std::vector<int>(nums.begin() + 3, nums.end());
                } else {
                    nums.clear();
                }
                nb_op++;
            }
            
            return nb_op;
        }
    };