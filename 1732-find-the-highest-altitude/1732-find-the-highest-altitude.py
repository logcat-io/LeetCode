class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        prefix = [0] * (n + 1)
        ans = 0
        for i in range(n):
            prefix[i+1] = prefix[i] + gain[i]
            if prefix[i+1] > ans:
                ans = prefix[i+1]
        
        return ans
        