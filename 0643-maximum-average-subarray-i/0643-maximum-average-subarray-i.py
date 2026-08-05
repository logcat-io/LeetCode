class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        wd = sum(nums[:k])
        max_sum = wd

        for i in range(k, len(nums)):
            wd += nums[i] - nums[i-k]
            max_sum = max(max_sum, wd)
        
        return max_sum / k


