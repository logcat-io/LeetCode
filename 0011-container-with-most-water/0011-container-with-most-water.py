class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        lo, hi = 0, len(height) - 1

        while lo < hi:
            s = (hi - lo) * min(height[lo], height[hi])

            ans = max(ans, s)

            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -=1
        
        return ans
        