class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # left = 0
        # n = len(nums)
        # right = 1
        
       
        # while right < n:
        #     nums[right] = nums[left] + nums[right] 
        #     right +=1
        #     left +=1
        # return nums

#         for right in range(1,n):
#             nums[right] = nums[right-1]+nums[right]
#             # left +=1
#         return nums
        
        
        
        
        
        
        
        
        
        
        
        
        
        prevSum, res = 0, []
        for i in nums:
            prevSum +=i
            res.append(prevSum)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
