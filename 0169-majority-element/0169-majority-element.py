class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(1) space
        count = 0
        for i in nums:
            if count == 0:
                candidate = i

            if candidate == i:
                count +=1
            else:
                count -=1
        return candidate





        # O(n) space

        # count = len(nums)//2
        # numMap = defaultdict(int)
        # for i in nums:
        #     numMap[i] +=1
        # for key,val in numMap.items():
        #     if val > count:
        #         return key
        # return -1
        