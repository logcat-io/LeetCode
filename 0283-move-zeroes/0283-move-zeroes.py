class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        lo, hi = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                lo = i
                hi = i+1
                break
        
        while hi < len(nums):
            if nums[hi] != 0:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi += 1
            else:
                hi += 1

        