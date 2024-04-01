class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative, positive,res = [],[],[]
        for i in range(len(nums)):
            if nums[i] < 0:
                negative.append(nums[i])
            else:
                positive.append(nums[i])
        for i in range(len(positive)):
            res.append(positive[i])
            res.append(negative[i])
        return res
        
                
        