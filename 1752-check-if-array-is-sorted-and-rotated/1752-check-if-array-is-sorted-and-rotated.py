class Solution:
    def check(self, nums: List[int]) -> bool:
#         sorted_nums = sorted(nums)
        
#         if nums == sorted_nums:
#             return True
#         for i in range(len(nums)-1):
#             if nums[i] > nums[i+1]:
#                 nums[:]= nums[i+1:] + nums[:i+1]
#         return nums == sorted_nums
    
        return sum(nums[i-1] > nums[i] for i in range(len(nums)))<= 1