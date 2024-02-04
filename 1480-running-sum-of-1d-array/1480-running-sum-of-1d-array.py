class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # Modifying nums in-place
        for i in nums(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
        
        # prevSum, res = 0, []
        # for i in nums:
        #     prevSum +=i
        #     res.append(prevSum)
        # return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
