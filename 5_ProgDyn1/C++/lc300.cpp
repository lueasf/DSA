#include <vector>
#include <algorithm>

// O(n²)
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        
        vector<int> length(n, 1);
        
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < k; i++) {
                if (nums[i] < nums[k]) {
                    length[k] = max(length[k], length[i] + 1);
                }
            }
        }
        
        return *max_element(length.begin(), length.end());
    }
};

// O(nlog(n))
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> lis;
        
        for (int num : nums) {
            auto it = lower_bound(lis.begin(), lis.end(), num);
            if (it == lis.end()) {
                lis.push_back(num);
            } else {
                *it = num;
            }
        }
        
        return lis.size();
    }
};