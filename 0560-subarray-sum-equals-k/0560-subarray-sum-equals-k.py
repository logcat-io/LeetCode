from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        memo = defaultdict(int)
        ans = 0

        # k = right - left
        memo[0] = 1
        right = 0
        for i in range(n):
            right += nums[i]
            ans += memo[right - k]
            memo[right] += 1

        return ans
