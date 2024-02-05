class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # kadane's
        


        # modified kadane's
        # maxprofit = 0
        # minbuy = prices[0]
        
        # for i in range(1, len(prices)):
        #     minbuy = min(minbuy, prices[i])
        #     maxprofit = max(maxprofit, prices[i]-minbuy)
        # return maxprofit


        # two pointer
        l, r = 0, 1
        # maxprofit = 0

        # while r<len(prices):
        #     if prices[l] < prices[r]:
        #         maxprofit = max(maxprofit, prices[r] - prices[l])
            
        #     else:
        #         l = r
        #     r +=1
        # return maxprofit

        






































        currMin, maxSoFar = float('inf'), 0
        for price in prices:
            currMin = min(currMin, price)
            maxSoFar = max(maxSoFar, price - currMin)
        return maxSoFar





         