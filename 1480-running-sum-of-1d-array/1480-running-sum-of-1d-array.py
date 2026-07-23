class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n
        left = 0

        for i in range(n):
            left += nums[i]
            ans[i] = left

        return ans
        