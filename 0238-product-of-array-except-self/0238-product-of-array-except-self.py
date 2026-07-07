class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        left  = [1] * (length + 1)
        for i, n in enumerate(nums):
            left[i+1] = left[i] * n
        
        right = [1] * (length + 1)
        for i , n in enumerate(nums[::-1]):
            right[i+1] = right[i] * n

        right = right[::-1]

        return [right[i+1] * left[i] for i in range(length)]
        