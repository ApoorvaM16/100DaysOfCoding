class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # numset = sorted(list(set(nums)))
        # # print(numset)
        # k = len(numset)
        # for i in range(k):
        #     nums[i]=numset[i]
        # return k

        j = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j +=1
        return j




        



        
