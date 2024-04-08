class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # practising using the set and finding the longest consecutive sequence
        count, numSet, maxcount = 0, set(), 0
        numSet.update(nums)
        for i in nums:
            if i-1 not in numSet:
                count = 1
                x = i
                while x+1 in numSet:
                    count +=1
                    x +=1
                maxcount = max(count, maxcount)
            else:
                count = 0
        return maxcount    
    
    
    
    
    
        