class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#   tc- nlogn+n 
        # nums = list(set(nums))
        # nums.sort()
        # n = len(nums)
        # if n == 0: return 0
        # count= maxcount = 1
        # print(nums)
        # for i in range(1, n):
        #     if nums[i-1] == nums[i] - 1:
        #         count +=1
        #         maxcount = max(count, maxcount)
            
        #     else:
                
        #         count = 1 
        # return maxcount   


        # if n == 0: return 0
        # numset, count, maxcount = set(), 0, 1
        # for i in nums:
        #     numset.add(i)
        # print(numset)
        # for i in numset:
        #     if i-1 not in numset:
        #         count =1
        #         x = i
        #         while x+1 in numset:
        #             count +=1 
        #             x +=1
        #         maxcount = max(count, maxcount)
        #     else:
        #         count = 0
        # return maxcount
      






        # Finding longest consecutive sequence with O(n) TC and O(n) SC
        n = len(nums)
        if n == 0: return 0
        numset, count, maxcount = set(), 0,1
        numset.update(nums)
        for i in numset:
            if i-1 not in numset:
                count = 1
                x = i
                while x+1 in numset:
                    count +=1
                    x +=1
                maxcount =  max(count, maxcount)
            else:
                count = 0
        return maxcount
