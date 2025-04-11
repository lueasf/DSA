#  Combinatorial Mathematics
## Solution of Editorial

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # Convert bounds to strings and adjust start by -1 to make the range inclusive
        start_ = str(start - 1)
        finish_ = str(finish)

        # The count is the valid numbers up to finish minus valid numbers before start
        return self.calculate(finish_, s, limit) - self.calculate(start_, s, limit)

    def calculate(self, x: str, s: str, limit: int):
        # If x has fewer digits than s, no number can contain s as suffix
        if len(x) < len(s):
            return 0
        # If x has same length as s, only valid if x >= s (only s itself is possible)
        if len(x) == len(s):
            return 1 if x >= s else 0
        # Extract the suffix part of x (same length as s)
        suffix = x[len(x) - len(s) :]
        count = 0
        # Length of the prefix (digits before the suffix)
        pre_len = len(x) - len(s)

        # Iterate through each digit in the prefix
        for i in range(pre_len):
            # If current digit exceeds limit, we can take all valid combinations
            # of remaining digits and return immediately
            if limit < int(x[i]):
                # (limit+1) options for each remaining digit
                count += (limit + 1) ** (pre_len - i)
                return count
            # Otherwise, count all numbers where:
            # - digits before i match x
            # - digit at i is less than x[i]
            # - remaining digits can be anything <= limit
            count += int(x[i]) * (limit + 1) ** (pre_len - 1 - i)

        # After checking all prefix digits, check if the suffix itself is valid
        if suffix >= s:
            count += 1

        return count

# Time complexity: O(log(finish))
