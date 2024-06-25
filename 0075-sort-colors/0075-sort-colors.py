class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        p1 = 0
        p2 = len(nums)-1
        while p <= p2:
            if nums[p] == 1:
                p +=1
            elif nums[p] > 1:
                nums[p2], nums[p] = nums[p],nums[p2]
                p2 -=1
            else:
                nums[p1], nums[p] = nums[p],nums[p1]
                p1 +=1
                p +=1
            
            