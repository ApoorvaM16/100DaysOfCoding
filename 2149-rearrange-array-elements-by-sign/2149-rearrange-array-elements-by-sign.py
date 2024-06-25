class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative,res = [], [], []
        for i in nums:
            if i > 0:
                positive.append(i)
            else:
                negative.append(i)
        for i in range(len(positive)):
            res.append(positive[i])
            res.append(negative[i])
        del positive,negative
        return res
        