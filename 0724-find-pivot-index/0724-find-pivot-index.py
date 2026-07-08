class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)

        left = [0] * (n+1)
        right = [0] * (n+1)

        for i in range(n):
            left[i+1] = left[i] + nums[i]
            right[n-i-1] = nums[n-i-1] + right[n-i]

        for i in range(n):
            if left[i] == right[i+1]:
                return i
        
        return -1

        