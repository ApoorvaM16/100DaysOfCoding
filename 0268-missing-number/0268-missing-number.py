class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # numMap = {}
        # for i in nums:
        #     numMap[i] = 1
        # for i in range(len(nums)+1):
        #     if i not in numMap.keys():
        #         return i
        
#         using math
        numSum = sum(nums)
        total = sum([i for i in range(len(nums)+1)])
        return total - numSum
                
            
        