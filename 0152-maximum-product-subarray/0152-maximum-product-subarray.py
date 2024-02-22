class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Dynamic programming approach 1
        # B = nums[::-1]
        # for i in range(1, len(nums)):
        #     nums[i] *=nums[i-1] or 1
        #     B[i] *=B[i-1] or 1
        # print(nums,B)    
        # return max(nums+B)



        # Dynamic Approach 2
        # prefix, suffix, maxSoFar = 0,0,float('-inf')

        # for i in range(len(nums)):
        #     prefix = (prefix or 1) * nums[i] 
        #     suffix =(suffix or 1) * nums[~i] 
        #     maxSoFar = max(maxSoFar, prefix,suffix)
        # return maxSoFar











        # temp = nums[::-1]
        # for i in range(1,len(nums)):
        #     nums[i] *= nums[i-1] or 1
        #     temp[i] *= temp[i-1] or 1
        # return max(nums + temp) 

        prefix, suffix, maxcount = 0,0, float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[~i]
            maxcount = max(prefix, suffix, maxcount)
        return maxcount



        


