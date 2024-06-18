class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in numMap:
                return [idx,numMap[diff]]
            else:
                numMap[val] = idx
                
        