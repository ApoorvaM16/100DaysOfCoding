class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
#         prefix, res, dic = 0, 0, {0:1}
       
#         for i in nums:
#             prefix +=i

#             if prefix-k in dic:
#                 res +=dic[prefix-k]

#             dic[prefix] = dic.get(prefix,0) +1  
#         return res


        prefix,res, dic = 0, 0, {0:1}
        for i in range(len(nums)):
            prefix +=nums[i]
            
            if prefix - k in dic:
                res += dic[prefix-k]
            dic[prefix] = dic.get(prefix, 0) + 1
        return res




                
#         Bruteforce
        # count = 0
        # for i in range(len(nums)):
        #     prefix = 0
        #     for j in range(i,len(nums)):
        #         prefix +=nums[j]
        #         if prefix == k:
        #             count +=1
        # return count
                
# Hashmap/Dictionary
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    