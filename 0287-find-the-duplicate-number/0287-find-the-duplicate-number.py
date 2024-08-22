class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we can use slow fast pointers to find cycles
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


        