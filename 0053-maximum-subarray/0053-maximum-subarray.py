class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's
        
        # curSum = 0
        # maxSoFar = float('-inf')

        # for i in nums:
        #     curSum = max(i, curSum+i)
        #     maxSoFar = max(maxSoFar, curSum)
        # return maxSoFar


        # Sliding window types
        # curSum = 0
        # maxSum = nums[0]

        # for i in nums:
        #     if curSum < 0:
        #         curSum = 0
        #     curSum += i
        #     maxSum = max(maxSum, curSum)
        # return maxSum







        curSum, maxSoFar = float('-inf'),float('-inf')
        for i in nums:
            curSum =max(i, curSum+i) 
            maxSoFar = max(curSum, maxSoFar)
        return maxSoFar   






        