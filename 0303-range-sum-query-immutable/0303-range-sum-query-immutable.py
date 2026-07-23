class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.array = [0] * (n + 1)

        for i in range(n):
            self.array[i+1] = self.array[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.array[right+1] - self.array[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)