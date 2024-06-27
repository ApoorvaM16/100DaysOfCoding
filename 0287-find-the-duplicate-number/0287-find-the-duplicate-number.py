class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         numMap = defaultdict(int)
#         for i in nums:
#             numMap[i] +=1
#         for key,val in numMap.items():
#             if val > 1:
#                 return key
        
    
#     constant space: using slow fast pointer
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break              #we have found the cycle, that tells duplicates are there
                
#         finding start of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow