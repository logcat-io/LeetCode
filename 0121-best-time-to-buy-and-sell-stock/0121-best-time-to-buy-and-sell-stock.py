class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right
            
            best = max(best, profit)
        
        return best
        