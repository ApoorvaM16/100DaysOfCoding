
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # linear time, linear space
        # numMap, n = defaultdict(int), len(nums)
        # for i in nums:
        #     numMap[i] += 1
        # for key, val in numMap.items():
        #     if val > n//2:
        #         return key
        
#         linear time, constant space
        candidate, count = 0,0
        for i in nums:
            if count == 0:
                candidate = i
            if i == candidate:
                count +=1
            else:
                count -=1
        return candidate
            
            
            
        