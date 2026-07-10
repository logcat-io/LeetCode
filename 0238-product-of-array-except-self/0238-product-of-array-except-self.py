class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] *  n

        left = nums[0]
        for i in range(1, n):
            ans[i] = ans[i-1] * left
            left = nums[i]
            print("left: ", left)

        right = 1
        for i in range(n-1,-1,-1):
            ans[i] *= right
            right *= nums[i]
        
        return ans
        