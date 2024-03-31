class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = maxsum = float('-inf')
        for i in nums:
            cursum = max(i, cursum+i)
            maxsum = max(cursum, maxsum)
        return maxsum
        