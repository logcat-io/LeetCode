class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        l = 0
        for i in range(n):
            if nums[l] != nums[i]:
                nums[l+1] = nums[i]
                l += 1
        return l+1
        