

# Time complexity:O(NLOGN)
# Space complexity:O(N)


class Solution:
    def longestSquareStreak(self, nums) -> int:
        max_len = -1
        nums_set = set(nums)
        sorted_nums = sorted(nums_set)

        for num in sorted_nums:
            count = 0
            curr = num
            while curr in nums_set:
                nums_set.remove(curr)
                curr = curr **2
                count += 1
            max_len = max(max_len, count)

        return max_len if max_len > 1 else -1
        

