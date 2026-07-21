class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = 0
        best = float('-inf')

        for right, v in enumerate(nums):
            window += v
            if right >= k - 1:
                best = max(best, window / k)
                window -= nums[right - k + 1]
        
        return best

        