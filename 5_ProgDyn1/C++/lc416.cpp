class Solution {
    public:
        bool canPartition(vector<int>& nums) {
            int tot_sum = accumulate(nums.begin(), nums.end(), 0);
    
            if (tot_sum % 2 != 0){
                return false;
            }
    
            int target = tot_sum / 2;
    
            unordered_set<int> dp;
            dp.insert(0);
    
            for (int i = nums.size() - 1; i >= 0; i--){
                unordered_set<int> dp2;
                for (int n : dp) {
                    int new_sum = nums[i] + n;
                    if (new_sum == target) {
                        return true;
                    }
                    dp2.insert(new_sum);
                    dp2.insert(n); 
                }
                dp = dp2;
            }
            return dp.count(target) > 0;
        }
    };