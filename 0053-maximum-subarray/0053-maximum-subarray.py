class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxsum = float('-inf')
        for i in nums:
            currSum = max(i, currSum + i)
            maxsum = max(currSum, maxsum)
        return maxsum
        