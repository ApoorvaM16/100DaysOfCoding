import math
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # dic = {}-------------------------------------------extra space
        # res = 0
        # for i in nums:
        #     if i in dic:
        #         res = i
        #     dic[i] = 1
        # del dic
        # return res

        # count--------------------------------------------------extra space
        # count = [0]*len(nums)
        # for num in nums:
        #     count[num] +=1
        #     if count[num] > 1:
        #         return num

        # modifying array element--------------------------------
        
        # for num in nums:
        #     idx = abs(num)
        #     if nums[idx] < 0:
        #         return idx
        #     nums[idx] = - nums[idx]
        # return 0


        #Fast and slow pointer: Floyd's Cycle Detection
        # slow= fast = nums[0]

        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break

        # slow = nums[0]
        # while slow !=fast:
        #     slow = nums[slow]
        #     fast = nums[fast]
        # return slow   




        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

            
        