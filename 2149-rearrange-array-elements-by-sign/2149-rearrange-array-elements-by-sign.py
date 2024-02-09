class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
#         even, odd = 0, 1
#         n = len(nums)
#         res = [0] *n 
#         for i in nums:
#             if i> 0:
#                 res[even] = i
#                 even +=2
#             if i < 0:
#                 res[odd] = i
#                 odd +=2
                     
#         return res
    
    
    


















        even, odd, res = [],[], []
        for i in nums:
            if i > 0:
                even.append(i)
            else:
                odd. append(i)
        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])
        return res




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        