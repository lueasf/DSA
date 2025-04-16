#  2537

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        left, pairs, ans = 0, 0, 0

        for num in nums:
            pairs += cnt[num]
            cnt[num] += 1
            while pairs >= k:
                cnt[nums[left]] -= 1
                pairs -= cnt[nums[left]]
                left += 1
            ans += left
        return ans

# Quand on fait ans += left, on compte tous les sous-tableaux qui se terminent à right et commencent à n'importe quel indice [0, left-1].
