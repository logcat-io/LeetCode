class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = middle = float('inf')

        for num in nums:
            if num <= left:
                left = num
            elif num <= middle:
                middle = num
            else:
                return True
        return False
        