class Solution {
    public:
        int minOperations(vector<int>& nums, int k) {
            unordered_set<int> s;
            for (int x : nums){
                if (x < k){
                    return -1;
                }else if (x > k){
                    s.insert(x);
                }
            }
            return s.size();
        }
    };