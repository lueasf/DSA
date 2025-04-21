// Count and Say 

class Solution {
public:
    string countAndSay(int n){
        string result = "1";

        for (int j = 1; j < n; ++j) {
            string current = "";
            int count = 1;
            for (int e = 1; e < result.size(); ++e) {
                if (result[e] == result[e - 1]) {
                    ++count;
                } else {
                    current += to_string(count) + result[e - 1];
                    count = 1;
                }
            }
            current += to_string(count) + result.back();
            result = current;
        }

        return result;
    }
};
