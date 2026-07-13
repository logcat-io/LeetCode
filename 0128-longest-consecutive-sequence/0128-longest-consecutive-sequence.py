class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sorted_nums = sorted(set(nums))

        ans = 0
        count = 1
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]+1:
                count += 1
            else:
                ans = max(ans, count)
                count = 1

        return max(ans, count)
        