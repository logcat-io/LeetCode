class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        prefix = 0
        
        for i in range(len(nums)):
            if i < k:
                prefix += nums[i]
            else:
                prefix -= nums[i-k]
                prefix += nums[i]
            
            if i >= k - 1:
                max_avg = max(max_avg, prefix / k)
        
        
        return max_avg


