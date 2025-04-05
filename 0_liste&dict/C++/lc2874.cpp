class Solution {
    public:
        long long maximumTripletValue(vector<int>& nums) {
            int n = nums.size();
            if (n < 3) return 0;
            
            vector<int> L(n,0);
            vector<int> R(n,0);
    
    
            for (int i = 0; i < n - 1; i++){
                L[i+1] = std::max(L[i], nums[i]);
                R[n - 2 - i] = std::max(R[n - 1 - i], nums[n - 1 - i]);
            }
    
            long long val = 0; 
            for (int i = 1; i < n-1; i++) {
                long long current = (long long)(L[i] - nums[i]) * R[i];
                if (current > val) {
                    val = current;
                }
            }
    
            return max(max_val, 0LL);
        }
    };