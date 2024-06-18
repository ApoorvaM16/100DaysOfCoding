class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         using dictionary
        # numMap = {}
        # for i in nums:
        #     if i in numMap:
        #         numMap[i] +=1
        #     else:
        #         numMap[i] = 1
        # for key, val in numMap.items():
        #     if val == 1:
        #         return key
            
        
        xor = 0;
        for i in nums:
            xor ^=i;
        return xor
            
        