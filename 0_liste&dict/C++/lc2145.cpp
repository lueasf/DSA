# Count The Hidden Sequences ( Medium )

class Solution {
public:
    int numberOfArrays(vector<int>& differences, int lower, int upper) {
        long long diff = 0;
        long long lowest = 0;
        long long highest = 0;

        for (int d : differences) {
            diff += d;
            lowest = min(lowest, diff);
            highest = max(highest, diff);

            if (highest - lowest > upper - lower) {
                return 0;
            }
        }
        return (upper - lower) - (highest - lowest) + 1;
    }
};
