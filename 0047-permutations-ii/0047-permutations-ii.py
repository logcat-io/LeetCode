class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, pos = [], []
        used = [False] * len(nums)

        def bt():
            if len(pos) == len(nums):
                res.append(pos[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                pos.append(nums[i])
                bt()
                pos.pop()
                used[i] = False
        
        bt()
        return res
        