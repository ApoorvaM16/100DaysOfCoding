class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = len(nums)//2
        numMap = defaultdict(int)
        for i in nums:
            numMap[i] +=1
        for key,val in numMap.items():
            if val > count:
                return key
        return -1
        