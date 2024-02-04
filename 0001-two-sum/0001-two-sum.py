class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dic = {}
        
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in dic:
        #         return [i, dic[diff]]
        #     else:
        #         dic[nums[i]] = i

        # dic ={}
        # for i, val in enumerate(nums):
        #     diff = target - val
        #     if diff in dic:
        #         return [i, dic[diff]]
        #     dic[val] = i






        numMap = defaultdict(int)
        for i, val in enumerate(nums):
            diff = target - val
            if diff in numMap:
                return [numMap[diff], i]
            else:
                numMap[val] = i
        

         













