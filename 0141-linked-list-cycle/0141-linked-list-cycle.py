# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # optimal: slow fast pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


        # if head is None or head.next is None:
        #     return False
        # LLmap, current ={}, head
        # while current:
        #     if current in LLmap:
        #         return True
        #     LLmap[current] = 1
        #     current = current.next
        # return False

        