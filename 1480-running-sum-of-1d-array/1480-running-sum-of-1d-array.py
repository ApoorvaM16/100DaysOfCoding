class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # res = [nums[0]]
        # for i in range(1,len(nums)):
        #     res.append(res[-1]+nums[i])
        # return res
    
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
            
        