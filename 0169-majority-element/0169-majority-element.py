class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # num_map = {}
        # for i in nums:
        #     if i not in num_map:
        #         num_map[i] = 1
        #     else:
        #         num_map[i] +=1
        #         if num_map[i] > len(nums)//2:
        #             return i
        # return i
    
    # moore algorithm
        count, candidate = 0,0
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count +=1
            else:
                count -=1
        return candidate
                
         
        