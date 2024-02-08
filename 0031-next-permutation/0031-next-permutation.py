class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the dip in the peak from backside
        # index = -1
        # n = len(nums)
        # for i in range(n-2,-1,-1):
        #     if nums[i] < nums[i+1]:
        #         index = i
        #         break
        # if index == -1:
        #     nums.reverse()
        #     return
        
        # # Swap next smallest
        # for i in range(n-1,-1,-1):
        #     if nums[i] > nums[index]:
        #         nums[i], nums[index] = nums[index], nums[i]
        #         break
         
        # #  sort the subarray
        # nums[index+1:] = nums[index +1:][::-1]


# practicing again
       
        index, n = -1, len(nums)
    # searching for the dip
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break
        if index == -1:
            nums.reverse()
            return
    # dip found, swap with next smallest number
        for i in range(n-1,-1,-1):
            if nums[i] > nums[index]:
               nums[i], nums[index] = nums[index], nums[i]
               break
    # sort the substring
        nums[index + 1: ] = nums[index + 1: ][::-1]
        







        