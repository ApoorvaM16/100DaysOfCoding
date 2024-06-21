class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = float('inf')
        maxprofit = float('-inf')
        for i in prices:
            sell = min(sell,i)
            maxprofit = max(i - sell, maxprofit)
        return maxprofit
        