class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)
        total = sum(nums)

        left = 0
        for i, v in enumerate(nums):
            right = total - left - v
            if left == right:
                return i
            left += v
        
        return -1

        