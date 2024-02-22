class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
                
        # res = []
        # nums.sort()
        # for i in range(n):
        #     if i >0 and nums[i] == nums[i-1]: continue
        #     j, k = i+1, n-1
        #     while j < k:
        #         tot = nums[i] + nums[j] +nums[k]
        #         if  tot< 0:
        #             j +=1
        #         elif tot > 0:
        #             k -=1
        #         else:
        #             res.append([nums[i], nums[j], nums[k]])
        #             j +=1
        #             k -=1
        #             while j < k and nums[j] == nums[j-1]: j+=1
        #             while j < k and nums[k] == nums[k+1]: k-=1
        
        # return res

        # Practice

# sort the array, i, j = i+1, k=n-1 add i,j,k, if it is 0, add it to res, check for 
# distinct j, k values, if sum>0, k-=1 else j+=1 anthe
        n, res = len(nums), []
        nums.sort()                # we are sorting because we want to reduce SC by not using set and the need to sort every output array
        for i in range(n):
            if i> 0 and nums[i] == nums[i-1]: continue 
            j, k = i+1, n-1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    k -=1
                    j +=1
                    while j<k and nums[j] == nums[j-1]: j +=1
                    while j<k and nums[k] == nums[k+1]: k -=1
            
                elif temp > 0: k -= 1
                else: j += 1              

        return res












































        