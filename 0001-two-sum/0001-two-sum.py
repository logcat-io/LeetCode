class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, v in enumerate(nums):
            if (target - v) in memo:
                return [i, memo[target-v]]
            
            memo[v] = i
