# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, arr = head, []
        while current:
            arr.append(current.val)
            current = current.next
        arr.sort()
        current = head
        for i in arr:
            current.val = i
            current = current.next
        return head
        