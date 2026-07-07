from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        ans = 0
        d[0] = 1
        prefix = 0

        for n in nums:
            prefix += n
            ans += d[prefix - k]
            d[prefix] += 1

        return ans
