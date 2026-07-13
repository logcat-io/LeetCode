from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sorted_nums = sorted(nums)
        count = defaultdict(int)

        for n in sorted_nums:
            if n - 1 in count:
                count[n] = count[n-1] + 1
            else:
                count[n] = 1

        return max(count.values())
        