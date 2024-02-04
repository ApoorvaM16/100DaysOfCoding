class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    #O(n) TC and O(n) SC
        # numMap = defaultdict(int)
        # for num in nums:
        #     numMap[num] += 1
        # for i in range(len(nums)+1):
        #     if i not in numMap:
        #         return i
        # return -1




        # maths broo    O(n) TC and O(1) SC
        numSum = sum(nums)
        total = sum([i for i in range(1,len(nums)+1)])
        return total-numSum




