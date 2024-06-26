class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numMap = defaultdict(int)
        for i in nums:
            numMap[i] +=1
        for key,val in numMap.items():
            if val > 1:
                return key
        