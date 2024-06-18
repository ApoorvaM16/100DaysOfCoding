class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, res = len(nums), []
        for i in range(n):
            if i > 0  and nums[i] == nums[i-1]: continue
            j, k = i + 1, n -1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j +=1
                    k -=1
                    while nums[j] == nums[j-1] and j < k: j +=1
                    while nums[k] == nums[k+1] and j< k: k -=1
                elif temp > 0:
                    k -= 1
                else:
                    j +=1
            
        return res
    