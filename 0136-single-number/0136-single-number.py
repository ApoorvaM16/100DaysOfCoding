class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        for i in nums:
            num_map[i] +=1
        for key, val in num_map.items():
            if val <2:
                return key
        