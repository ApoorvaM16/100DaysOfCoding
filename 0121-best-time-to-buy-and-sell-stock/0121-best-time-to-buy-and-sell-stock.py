class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currProfit, maxProfit = float('inf'),0
        for i in range(len(prices)):
            currProfit = min(currProfit, prices[i])
            maxProfit = max(prices[i]-currProfit, maxProfit)
        return maxProfit
        