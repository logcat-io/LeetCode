from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        memo = defaultdict(int)
        memo[0] = 1
        # k = prefix[r+1] - prefix[l]
        # prefix[r+1] - k = prefix[l]
        
        prefix = 0

        for i in range(n):
            prefix += nums[i]
            ans += memo[prefix - k]
            memo[prefix] += 1
        
        return ans
