class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        
        # total = left + nums[i] + right
        left = 0
        for i in range(n):
            right = total - nums[i] - left
            if left == right:
                return i
            
            left += nums[i]

        return -1

        