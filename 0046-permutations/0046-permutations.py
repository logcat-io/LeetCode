class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, pos = [], []
        used = [False] * len(nums)

        def bt():
            if len(pos) == len(nums):
                res.append(pos[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                pos.append(nums[i])
                bt()
                pos.pop()
                used[i] = False
        
        bt()
        return res
        