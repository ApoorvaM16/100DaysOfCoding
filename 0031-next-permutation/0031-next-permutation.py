class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n, index = len(nums), -1
        # finding the dip
        for i in range(n-1,-1,-1):
            if nums[i] > nums[i-1]:
                # nums[i], nums[i-1] = nums[i-1], nums[i]
                index = i-1
                break
        if index == -1:
            nums.reverse()
            return
        # dip found, swapping to get the least next element
        for i in range(n-1,-1,-1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
            
        # sorting to get the next permutation
        nums[index+1:] = nums[index+1:][::-1]
        
        
        
#           index, n = -1, len(nums)
#     # searching for the dip
#         for i in range(n-2, -1, -1):
#             if nums[i] < nums[i+1]:
#                 index = i
#                 break
#         if index == -1:
#             nums.reverse()
#             return
#     # dip found, swap with next smallest number
#         for i in range(n-1,-1,-1):
#             if nums[i] > nums[index]:
#                nums[i], nums[index] = nums[index], nums[i]
#                break
#     # sort the substring
#         nums[index + 1: ] = nums[index + 1: ][::-1]
        