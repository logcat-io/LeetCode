class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        left = 0
        # total = right + nums[i] + left
        for i in range(n):
            right = total - nums[i] - left

            if right == left:
                return i
            
            left += nums[i]

        return -1

        