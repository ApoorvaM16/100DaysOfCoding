class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        n = len(nums)
        p1,p,p2 = 0,0,n-1
        while p <= p2:
            if nums[p] < 1:
                nums[p], nums[p1] = nums[p1], nums[p]
                p1 +=1
                p +=1
            elif nums[p] == 1:
                p +=1
                # continue
            else:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -=1
                # p +=1
                             
        
        
        # n = len(nums)
        # p1,p,p2 = 0,0,n-1                       #p1:red, p:white, p2:blue
        # while p <= p2:
        #     if nums[p] == 0:
        #         nums[p], nums[p1] = nums[p1], nums[p]
        #         p +=1
        #         p1 +=1
        #     elif nums[p] ==1:
        #         p +=1
        #     else:
        #         nums[p], nums[p2] = nums[p2], nums[p]
        #         p2 -=1
                