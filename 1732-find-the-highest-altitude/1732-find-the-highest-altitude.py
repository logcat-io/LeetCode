class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        prefix = [0] * (n + 1)
        ans = 0
        
        for i in range(n):
            prefix[i+1] = prefix[i] + gain[i]
            ans = max(prefix[i+1], ans)
        
        return max(ans, 0)
        