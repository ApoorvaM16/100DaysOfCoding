
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMap, n = defaultdict(int), len(nums)
        for i in nums:
            numMap[i] += 1
        for key, val in numMap.items():
            if val > n//2:
                return key
            
            
            
        