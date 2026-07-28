class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, pos = set(), []
        used = [False] * len(nums)

        def bt():
            if len(pos) == len(nums):
                res.add(tuple(pos[:]))
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
        return list(res)
        