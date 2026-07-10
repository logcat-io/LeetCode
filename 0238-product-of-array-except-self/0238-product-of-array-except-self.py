class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] *  n
        
        # except self 를 제외하는데 집중하면 된다.

        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1,-1,-1):
            ans[i] *= right
            right *= nums[i]
        
        return ans
        