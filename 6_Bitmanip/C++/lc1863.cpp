#include <vector>
using namespace std;

class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        vector<int> res;
        dfs(0, nums, {}, res);
        int sum = 0;
        for (int num : res) {
            sum += num;
        }
        return sum;
    }

private:
    void dfs(int start, vector<int>& arr, vector<int> current, vector<int>& res) {
        int x = 0;
        for (int num : current) {
            x ^= num;
        }
        res.push_back(x);

        for (int i = start; i < arr.size(); i++) {
            current.push_back(arr[i]);
            dfs(i + 1, arr, current, res);
            current.pop_back();
        }
    }
};