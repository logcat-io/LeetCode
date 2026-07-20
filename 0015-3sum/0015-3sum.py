class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]

                if s == 0:
                    res.append([nums[i], nums[lo], nums[hi]])

                    lv = nums[lo]
                    while lo < hi and nums[lo] == lv:
                        lo += 1
                    
                    hv = nums[hi]
                    while lo < hi and nums[hi] == hv:
                        hi -= 1
                elif s > 0:
                    hi -= 1
                else:
                    lo += 1

        
        return res
        
        