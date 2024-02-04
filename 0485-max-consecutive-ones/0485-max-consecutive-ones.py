class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # count = maxCount= 0

        # for i in nums:
        #     if i != 1:
        #         count = 0
        #     else:
        #         count +=1
        #         maxCount = max(count, maxCount)
                
        # return maxCount

        # using math brooo
        
        maxCount = count = 0
        for i in nums:
            count =count*i + i
            maxCount = max(count, maxCount)
        return maxCount










        # maxcount, count = 0, 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]==1:
        #         count +=1
        #         maxcount = max(count, maxcount)
        #     else:
        #         count = 1
        # return maxcount