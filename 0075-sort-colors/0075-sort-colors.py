class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        left = 0
        right = 1

        for i in range(3):
            right = left + 1

            while right < n:
                if nums[left] == i:
                    left += 1
                    right = left + 1
                    continue

                if nums[right] == i:
                    nums[right], nums[left] = nums[left], nums[right]
                    left += 1
                
                right += 1
            
            


            
        