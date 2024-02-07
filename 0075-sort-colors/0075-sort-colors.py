class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dic = {}
        # nums1 = []
        # for i in nums:
        #     if i in dic:
        #         dic[i] +=1
        #     else:
        #         dic[i] = 1
        
        # for i in range(3):
        #     if i in dic:
        #         nums1[:] += [i] * dic[i]
        # nums[:] = nums1
        


        numMap,res = defaultdict(int), []
        for i in nums:
            numMap[i] +=1
        
        for i in range(3):
            res+=[i] * numMap[i]
        nums[:] = res