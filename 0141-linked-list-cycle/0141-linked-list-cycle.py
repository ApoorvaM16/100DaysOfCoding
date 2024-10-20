# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        LLmap, current ={}, head
        while current:
            if current in LLmap:
                return True
            LLmap[current] = 1
            current = current.next
        return False

        