class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix, numMap, res = 0, {0: 1}, 0
        for i in nums:
            prefix +=i
            
            if prefix - k in numMap:
                res += numMap[prefix-k]
            if prefix in numMap:
                numMap[prefix] +=1
            else:
                numMap[prefix] = 1
        return res
                
        
        
#         prefix,res, dic = 0, 0, {0:1}
#         for i in range(len(nums)):
#             prefix +=nums[i]
            
#             if prefix - k in dic:
#                 res += dic[prefix-k]
#             dic[prefix] = dic.get(prefix, 0) + 1
#         return res
        