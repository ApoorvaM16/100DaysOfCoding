class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # total = sum(nums)
        # leftsum = 0
        # for i in range(len(nums)):
        #     rightsum = total-leftsum-nums[i]
        #     if rightsum == leftsum:
        #         return i
        #     leftsum +=nums[i]
        # return -1








        leftSum, total = 0, sum(nums)
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum +=nums[i]
        return -1














