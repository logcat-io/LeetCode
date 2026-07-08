class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] *  n

        left = 1
        for i, v in enumerate(nums):
            ans[i] = left
            left *= v
        
        right = 1
        for i in range(n -1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans
        